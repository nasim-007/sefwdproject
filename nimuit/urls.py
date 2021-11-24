from django.urls import path
from . import views
app_name = 'nimuit'

urlpatterns = [
    
    path('', views.index, name='index'),
    path('it-solution/', views.itsolution, name='itsolution'),
    path('contact_form/', views.contact, name='contact_form'),
    path('search/', views.search, name='search'),
]