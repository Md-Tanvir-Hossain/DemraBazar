from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import  index, activate

urlpatterns=[
    path('',views.index,name='index'),
    path('about_us',views.about_us,name='about_us'),
    path('tictoc',views.tictoc,name='tictoc'),
    path('login/',views.loginPage,name='login'),
    path('register/',views.register,name='register'),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/', activate, name='activate'),
    path('logout/',views.logoutP,name='logout'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('post_job/',views.post_job_page,name='post_job'),
    path('job/',views.job_page,name='job'),
    path('job_page_single/<str:pk>',views.job_page_single,name='job_page_single'),
    path('post_product/',views.post_product_page,name='post_product'),
    path('product/',views.product_page,name='product'),
    path('product_page_single/<str:pk>',views.product_page_single,name='product_page_single'),
    path('forget/',views.forgetPage,name='forget'),
    path('delete_product/<int:pk>',views.delete_product , name = 'delete_product'),
    path('delete_job/<int:pk>',views.delete_job, name = 'delete_job'),
    path('search',views.search,name='search'),
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name = "registration/password_reset_forms.html"),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name = "registration/password_reset_dones.html"),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name = "registration/password_reset_confirms.html"),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name = "registration/password_reset_completes.html"),name='password_reset_complete'),
    path('contact',views.contact,name='contact'),
    path('email_verification/',views.email_verification,name='email_verification'),
    path('invalid_email_verification/',views.invalid_email_verification,name='invalid_email_verification'),
    path('Check_email_to_verify/',views.response_email_verification,name='verify_your_email'),
]