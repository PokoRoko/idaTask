from django.urls import path
from . import views

app_name = 'image'
urlpatterns = [
    path('load_image', views.form_upload, name='load_image'),

    path('', views.list_image, name='list_image'),
]

