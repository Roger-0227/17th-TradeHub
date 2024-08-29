from django.urls import path

from . import views

app_name = "suppliers"

urlpatterns = [
    path("", views.index, name="index"),
    path("new", views.new, name="new"),
    path("show/<int:id>", views.show, name="show"),
]
