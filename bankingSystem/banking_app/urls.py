from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="Home"),
    path("customer",views.customer,name="customer"),
    path("transaction",views.transaction,name="trans"),
    path("about",views.about,name="about")
]