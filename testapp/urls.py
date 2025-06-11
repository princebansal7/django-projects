from django.urls import path
from testapp import views

urlpatterns = [
    path("greeting/", views.greeting),
    path("about/", views.about),
    path("contact/", views.contact),
]
