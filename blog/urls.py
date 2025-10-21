from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.index, name="index"),
    path("posts/<slug:slug>/", views.detail, name="detail"),
    path("old-url/", views.old_url_redirect, name="old-url"),
    path("diff-new-url/", views.new_url_view, name="new-url"),
    path("contact", views.contact_view, name="contact"),
    path("about", views.about_view, name="about"),
]