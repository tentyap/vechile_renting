from django.urls import path
from . import views

urlpatterns = [
    path("create", views.CustomerCreateAPIView.as_view(), name="create"),
    path("edit", views.CustomerEditApiview.as_view(), name="edit"),
    path("delete", views.CustomerDeleteApiview.as_view(), name="delete"),
    path("list", views.CustomerListApiview.as_view(), name="list"),

]