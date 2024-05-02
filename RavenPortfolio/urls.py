from django.urls import path
from .views import Home,About,Hobbies,Contacts

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("about", About.as_view(), name="about"),
    path("hobbies", Hobbies.as_view(), name="hobbies"),
    path("contacts", Contacts.as_view(), name="contacts"),
]
