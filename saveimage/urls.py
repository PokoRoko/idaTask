from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls import url, static

app_name = 'image'
urlpatterns = [
    path('load_image', views.form_upload, name='load_image'),
    path('form_resize', views.form_resize, name='form_resize'),
    path('', views.list_image, name='list_image'),
]

