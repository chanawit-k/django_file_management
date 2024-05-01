from django.urls import path
from . import views

app_name = 'uploadfile'


urlpatterns = [
    path('', views.TestTemplateView.as_view(), name='test'),
    path('create', views.EmployeeCreateView.as_view(), name='employee_create'),
]