from django.views.generic import TemplateView

class TestTemplateView(TemplateView):
    template_name = 'uploadfile/test_template.html'