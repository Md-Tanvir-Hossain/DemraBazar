from django.contrib import admin
from .models import Contact
from .models import JobsData
from .models import ProductData
#HTML
admin.site.login_template = "admin/admin_logIn.html"
admin.site.index_title = "DemraBazar Data Base"
admin.site.site_header = "DemraBazar Admin"
admin.site.site_title = "DemraBazar"

# Register your models here.

admin.site.register(Contact)
admin.site.register(JobsData)
admin.site.register(ProductData)