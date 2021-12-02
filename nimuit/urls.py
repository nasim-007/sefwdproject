from django.urls import path
from . import views
app_name = 'nimuit'

urlpatterns = [
    
    path('', views.index, name='index'),
    path('it-solution/', views.itsolution, name='itsolution'),
    path('about_us/', views.about_us, name='about'),
    path('contact_us/', views.contact_us, name='contact'),
    path('blog/', views.blog_index, name='blog_index'),
    path('blog/<slug>/', views.blog_details, name='blog_details'),

    path('contact_form/', views.contact, name='contact_form'),
    path('search/', views.search, name='search'),
]