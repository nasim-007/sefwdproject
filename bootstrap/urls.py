from django.urls import path
from . import views
from .views import AddAlbum, Delete, Update
app_name = 'bootstrap'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.AddAlbum.as_view(), name='create'),
    path('<int:id>/delete/', views.Delete.as_view(), name='delete'),
    path('<int:id>/update/', views.Update.as_view(), name='update'),
]