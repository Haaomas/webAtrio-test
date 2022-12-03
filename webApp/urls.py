from django.urls import path

from . import views

# app_name to avoid namespace collision
app_name = "webApp"

urlpatterns = [
    path("", views.AddPersonFormView.as_view(
        success_url="success"), name="add_person"),
    path("success", views.success, name="success"),
    path("listView", views.IndexView.as_view(), name="index"),
]
