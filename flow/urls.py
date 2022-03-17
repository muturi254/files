from django.urls import path
from flow import views

urlpatterns = [
    path('', views.index, name='index'),
    path('files/', views.file_upload, name='file_upload'),
    path('files/<int:pk>', views.document_view, name='document_view'),
    path('files/<int:pk>/edit', views.edit_view, name='edit_view'),
]