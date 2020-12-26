from django.conf.urls import url
from django.urls import path, re_path
from . import views

app_name = 'image'
urlpatterns = [
    re_path(r'^load_image/(?P<open_image>\S+)/', views.form_upload),
    path('load_image', views.form_upload, name='load_image'),
    path('', views.list_image, name='list_image'),
]

