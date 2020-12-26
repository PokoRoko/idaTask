from django.urls import path, re_path
from . import views

app_name = 'image'
urlpatterns = [
    re_path(r'^resize/(?P<open_image>\S+)/', views.resize, name='resize'),
    path('resize/', views.resize, name='resize'),
    path('load_image', views.form_upload, name='load_image'),
    path('', views.list_image, name='list_image'),
]

