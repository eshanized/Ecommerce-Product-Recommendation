from django.contrib import admin
from .models import CompanyAddress, CompanyDetails

# Register your models here.
admin.site.register([ CompanyAddress, CompanyDetails])
