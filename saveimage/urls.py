from django.urls import path
from . import views


app_name = 'image'
urlpatterns = [
    path('', views.form_upload, name='load_image'),
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]

