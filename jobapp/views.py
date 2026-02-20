from itertools import product
from django.shortcuts import render,redirect
from django.http import HttpResponse, request
from django.db.models import Q
import datetime
from django.core.files.storage import default_storage
from django.contrib.auth.models import User
import time
import json
from collections import OrderedDict
import json
# from django.contrib.auth.forms import UserCreationForm
# Create your views here.
# from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import *
from jobapp.models import JobsData
from jobapp.models import ProductData
from .models import Contact
import uuid
from django.contrib.sites.shortcuts import get_current_site  
from django.utils.encoding import force_bytes
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode  
from django.template.loader import render_to_string  
from .tokens import account_activation_token 
from django.core.mail import EmailMessage  
from django.contrib.auth import get_user_model
from django.http import HttpResponse

def index(request):
    return render(request,'jobapp/index.html',{})
def about_us(request):
    return render(request,'jobapp/about_us.html',{})
def tictoc(request):
    return render(request,'jobapp/tictoc.html',{})

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password =request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            print("USER",user)
            if user is not None:
                login(request, user)
                print("LOGGED IN")
                # logout(request)
                return redirect('index')
            else:
                messages.info(request, 'Username OR password is incorrect')
        context = {}
        return render(request, 'jobapp/login_signup.html', context)

def register(request):
    if request.method == 'POST':
        users = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_obj = User.objects.create_user(username=users, email=email, password=password)
        user_obj.first_name = users
        user_obj.is_superuser = False
        user_obj.is_active = False
        user_obj.save()
        current_site = get_current_site(request)  
        mail_subject = 'Activation link has been sent to your email id'   
        message = render_to_string('jobapp/acc_active_email.html', {  
                'user': user_obj,  
                'domain': current_site.domain,  
                'uid':urlsafe_base64_encode(force_bytes(user_obj.pk)),  
                'token':account_activation_token.make_token(user_obj),
                "protocol": 'https' if request.is_secure() else 'http'  
            })  
        to_email = user_obj.email  
        email = EmailMessage(  
                         mail_subject, message, to=[to_email]  
            )  
        email.send()  
        messages.success(request,"Please confirm your email address to complete the registration")
        return redirect('verify_your_email')

def logoutP(request):
    logout(request)
    return redirect('index')


def dashboard(request):
    user_name = request.user.first_name
    all_user = len(User.objects.all())
    all_job = len(JobsData.objects.all())
    all_product = len(ProductData.objects.all())

    context = {'user_name':user_name,'all_user':all_user,'all_job':all_job,'all_product':all_product}
    return render(request,'jobapp/dashboard.html',context)

def post_job_page(request):
    if request.method == 'POST':
        job_title = request.POST['job_title']
        job_description = request.POST['job_description']
        job_city = request.POST['job_city']
        job_city_postal = request.POST['job_city_postal']
        company_name = request.POST['company_name']
        email_to_apply = request.POST['email_to_apply']
        user_posted = request.POST['user_posted']
        employment_type = request.POST['employment_type']
        user_id = request.user.id
        print(request.POST)
        job_obj = JobsData.objects.create(job_title=job_title,job_description=job_description,job_city=job_city,
                                          job_city_postal=job_city_postal,company_name=company_name,email_to_apply=email_to_apply,
                                          user_posted=user_posted,employment_type=employment_type,user_id=user_id)
        job_obj.save()
        return redirect('job')

    user_name = request.user.first_name
    context = {'user_name':user_name}
    return render(request, 'jobapp/post_job_page.html', context)

def job_page(request):
    user_name = request.user.first_name
    all_job = JobsData.objects.all()
    context = {'user_name':user_name,'all_job':all_job}
    return render(request, 'jobapp/job_form.html', context)

def job_page_single(request,pk):
    user_name = request.user.first_name
    job_data = JobsData.objects.filter(id=int(pk))
    context = {'user_name':user_name,'job_data':job_data}
    return render(request, 'jobapp/job_single.html', context)


def post_product_page(request):
   if request.method == 'POST':

        product_title = request.POST['product_title']
        product_description = request.POST['product_description']
        brand = request.POST['brand']
        stock = request.POST['stock']
        contact_number = request.POST['contact_number']
        user_posted = request.POST['user_posted']
        product_type = request.POST['product_type']
        price = request.POST['price']
        user_id = request.user.id
        product_image = request.FILES['imageUpload']
        print(request.POST)
        product_obj = ProductData.objects.create(product_title=product_title,product_description=product_description,contact_number=contact_number,brand=brand,
                                       stock=stock,user_posted=user_posted,price=price,type=product_type,user_id=user_id,product_image=product_image)
        product_obj.save()
        return redirect('product')
   user_name = request.user.first_name
   context = {'user_name':user_name}
   return render(request, 'jobapp/post_product_page.html',context)

def product_page(request):
    user_name = request.user.first_name
    all_products = ProductData.objects.all()
    context = {'user_name':user_name,'all_products':all_products}
    return render(request, 'jobapp/product_all.html', context)

def product_page_single(request,pk):
    user_name = request.user.first_name
    product_data = ProductData.objects.filter(id=int(pk))
    context = {'user_name':user_name,'product_data':product_data}
    print(product_data)
    return render(request, 'jobapp/product_single.html', context)
def forgetPage(request):
    
    return render(request, 'jobapp/forget.html',{})

def delete_product(requst,pk):
    product =ProductData.objects.get(id=pk)
    product.delete()
    return redirect('product')

def delete_job(requst,pk):
    job =JobsData.objects.get(id=pk)
    job.delete()
    return redirect('job')

def search(request):
    query = request.GET['query']
    all_job = JobsData.objects.filter(job_title__icontains=query)
    all_products = ProductData.objects.filter(product_title__icontains=query)
    context = {'all_job': all_job, 'all_products':all_products}
    return render(request, 'jobapp/search.html', context)

def contact(request):
    if request.method=='POST':
       name = request.POST['name']
       mail = request.POST['mail']
       subject = request.POST['subject']
       message = request.POST['message']
       contact=Contact(name=name,mail=mail,subject=subject,message=message)
       contact.save()
    return render(request, 'jobapp/contact.html')

def email_verification(request):
    return render(request,'jobapp/email_verification.html',{})

def invalid_email_verification(request):
    return render(request,'jobapp/invalid_email_verification.html',{})

def activate(request, uidb64, token):  
    User = get_user_model()  
    try:  
        uid = force_str(urlsafe_base64_decode(uidb64))  
        user = User.objects.get(pk=uid)  
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):  
        user = None  
    if user is not None and account_activation_token.check_token(user, token):  
        user.is_active = True  
        user.save()  
        return redirect('email_verification')
    #HttpResponse('Thank you for your email confirmation. Now you can login your account.')  
    else:  
        return redirect('invalid_email_verification')
    #HttpResponse('Activation link is invalid!')
    
def response_email_verification(request):
    return render(request, 'jobapp/httprseponse_email_varification.html',{})