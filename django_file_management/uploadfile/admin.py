from django.contrib import admin

from .models import Employee, EmployeeCertificate

# Register your models here.
admin.site.register(Employee)
admin.site.register(EmployeeCertificate)