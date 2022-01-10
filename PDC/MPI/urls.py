from django.urls import path
from MPI import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path("userDetails/", views.userDetails, name="userDeatils")
]