from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect
import os
from .models import EmployeeCertificate
from .forms import EmployeeForm
from django.conf import settings


class TestTemplateView(TemplateView):
    template_name = 'uploadfile/test_template.html'


class EmployeeCreateView(CreateView):
    template_name = 'uploadfile/employee_create.html'
    form_class = EmployeeForm
    success_url = reverse_lazy('uploadfile:employee_create')

    def form_valid(self, form):
        employee = form.save(commit=False)
        pan_card_pic = self.request.FILES.get('pan_card_pic_blob')
        if pan_card_pic:
            employee.pan_card_pic_blob = pan_card_pic.read()

        employee.save()

        certificate_files = self.request.FILES.getlist('certificate_files')
        if len(certificate_files) > 2:
            messages.error(
                self.request, 'You can upload a maximum of 10 certificate files.')
            return redirect('uploadfile:employee_create')

        # Create a folder for the employee using employee id
        employee_folder = os.path.join(settings.MEDIA_ROOT, 'employee_files', 'certificates', str(employee.id))
        os.makedirs(employee_folder, exist_ok=True)

        for idx, certificate_file in enumerate(certificate_files, start=1):
            original_extension = os.path.splitext(certificate_file.name)[1]

            # Rename and save the certificate file with the desired format
            new_filename = f'{employee.id}_{employee.first_name}_{idx}{original_extension}'
            new_file_path = os.path.join(employee_folder, new_filename)
            print(f' file path : {new_file_path}')
            # Save the certificate file
            with open(new_file_path, 'wb+') as destination:
                for chunk in certificate_file.chunks():
                    destination.write(chunk)
            relative_file_path = os.path.relpath(new_file_path, settings.MEDIA_ROOT)
            print(f' file path after with  : {new_file_path}')
            EmployeeCertificate.objects.create(
                employee=employee,
                certificate_file=relative_file_path,  # Save the path, not the File object
            )
        return super().form_valid(form)
