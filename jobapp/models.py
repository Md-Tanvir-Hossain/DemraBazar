from django.db import models
from django_celery_beat.models import PeriodicTask
# Create your models here.

class JobsData(models.Model):
    emp_type = [
        ('Full-Time', 'Full-Time'),
        ('Part-Time', 'Part-Time'),
        ('Internship', 'Internship'),
        ('Contract', 'Contract'),
    ]

    job_title = models.CharField(max_length=1000000000,null=True)
    job_description = models.CharField(max_length=1000000000,null=True)
    job_city = models.CharField(max_length=1000000000,null=True)
    job_city_postal = models.CharField(max_length=1000000000,null=True)
    company_name = models.CharField(max_length=1000000000,null=True)
    email_to_apply = models.CharField(max_length=1000000000,null=True)
    user_posted = models.CharField(max_length=1000000000,null=True)
    employment_type = models.CharField(max_length=1000000000,choices=emp_type,null=True)
    user_id = models.CharField(max_length=10000000000,null=True)


class ProductData(models.Model):
    product_type = [
        ('Electronics', 'Electronics'),
        ('Clothing/Fashion', 'Clothing and Fashion'),
        ('Stationery', 'Stationery'),
        ('Beverages', 'Beverages'),
        ('Pets', 'Pets'),
        ('Jewelry', 'Jewelry'),
        ('Home-Furniture', 'Home-Furniture'),
        ('Beauty', 'Beauty'),
        ('Books/Media', 'Books/Media'),
        ('Toys/Games', 'Toys/Games'),
        ('Health/Wellness', 'Health/Wellness'),
        ('Automotive', 'Automotive'),
        ('Home-Improvement', 'Home-Improvement'),
        ('Sports/Outdoors', 'Sports/Outdoors'),
    ]

    product_title = models.CharField(max_length=1000000000,null=True)
    product_description = models.CharField(max_length=1000000000,null=True)
    brand = models.CharField(max_length=1000000000,null=True)
    price = models.CharField(max_length=1000000000,null=True)
    stock = models.CharField(max_length=1000000000,null=True)
    user_posted = models.CharField(max_length=1000000000,null=True)
    type = models.CharField(max_length=1000000000,choices=product_type,null=True)
    user_id = models.CharField(max_length=10000000000,null=True)
    contact_number = models.CharField(max_length=10000000000,null=True)
    product_image = models.ImageField(upload_to="product_images/",null= True, blank= True)
    

class Contact(models.Model):
    Serial = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    mail = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    Time = models.DateTimeField(auto_now_add=True , blank=True)
    
    
    class Monitor(models.Model):

    # monitored endpoint
    endpoint = models.CharField(max_length=1024, blank=False)

    # interval in seconds
    # enpoint will be checked every specified interval time period
    interval = models.IntegerField(blank=False)

    task = models.OneToOneField(
        PeriodicTask, null=True, blank=True, on_delete=models.SET_NULL
    )

    created_at = models.DateTimeField(auto_now_add=True)


class MonitorRequest(models.Model):

    # endpoint response time in miliseconds
    response_time = models.IntegerField(blank=False)

    response_status = models.IntegerField(blank=False)

    monitor = models.ForeignKey(Monitor, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

