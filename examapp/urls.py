from django.urls import path
from examapp import views

urlpatterns = [
    path("testpaper/", views.testpaper),
    path("mcq/", views.mcq),
]
