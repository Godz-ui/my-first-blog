from django.urls import path, re_path, include
from . import views


product_patterns = [
    path("", views.products),
    path("new", views.new),
    path("top", views.top),
    path("comments", views.comments),
    path("questions", views.questions),
    ]

urlpatterns = [

    re_path(r"^user/(?P<name>\D+)/(?P<age>\d+)", views.user),
    re_path(r"^user/(?P<name>\D+)", views.user),
    re_path(r"^user", views.user),
    path("products/<int:id>/", include(product_patterns)),

    path("", views.index),

    path("about/", views.about),
    path("contact/", views.contact),
    path("details/", views.details),

    path("index/<int:id>", views.index),
    path("access/<int:age>", views.access),
]