from django.db import models
import os


class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    cv_file = models.FileField(upload_to='employee_files/cv/', null=True, blank=True)
    photo_file = models.FileField(upload_to='employee_files/photo/', null=True, blank=True)

def certificate_upload_path(instance, filename):
    return os.path.join('employee_files', 'certificates', str(instance.employee.id), filename)

class EmployeeCertificate(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    certificate_file = models.FileField(upload_to=certificate_upload_path, null=True, blank=True)

    def __str__(self):
        return f"{self.employee}"