from django.views.generic import TemplateView

class Home(TemplateView):
    template_name = "pages/home.html"

class About(TemplateView):
    template_name = "pages/about.html"

class Hobbies(TemplateView):
    template_name = "pages/hobbies.html"

class Contacts(TemplateView):
    template_name = "pages/contacts.html"