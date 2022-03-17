from django.urls import path
from flow import views

urlpatterns = [
    path('', views.index, name='index'),
    path('files/', views.file_upload, name='file_upload',)
]