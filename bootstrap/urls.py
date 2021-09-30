from django.urls import path
from . import views

app_name = 'bootstrap'

urlpatterns = [
    path('', views.index, name='index'),

]