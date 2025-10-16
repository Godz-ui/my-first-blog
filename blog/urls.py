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
    path('', views.post_list, name='post_list'),
    path('info', views.info_list, name='info_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),

    path('index/<str:name>/<int:age>', views.index),

    # re_path(r"^user/(?P<name>\D+)/(?P<age>\d+)", views.user),
    # re_path(r"^user/(?P<name>\D+)", views.user),
    # re_path(r"^user", views.user),
    # path("products/<int:id>/", include(product_patterns)),



    path("about/", views.about),
    path("contact/", views.contact),
    path("details/", views.details),

    # path("index/<int:id>", views.index),
    path("access/<int:age>", views.access),
]