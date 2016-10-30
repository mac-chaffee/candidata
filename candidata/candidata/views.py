from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = 'home.html'


class Results(TemplateView):
    template_name = 'results.html'
