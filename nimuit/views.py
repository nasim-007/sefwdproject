from django.shortcuts import render
from .models import Expert, Project, Testimonial, Service, Partner, Award
from .forms import AppointmentForm, ContactForm
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView
from django.db.models import Q
from django.contrib import messages
# Create your views here.

def index(request):

    experts = Expert.objects.all()
    projects = Project.objects.all()
    testimonials = Testimonial.objects.all()
    services = Service.objects.all()
    partners = Partner.objects.all()
    awards = Award.objects.all()
    
    if request.method == 'POST':
        
        appoint_form = AppointmentForm(request.POST)
        
        
        if appoint_form.is_valid():
            
            appoint_form.save()
            messages.success(request, 'You booked an appointment.')
            # redirect to a new URL:
            return HttpResponseRedirect(request.path_info)
        
        
        
        
    
    
    # if a GET (or any other method) we'll create a blank form
    else:
        appoint_form = AppointmentForm()
        


    
    
    
    context = {

        'experts': experts,
        'projects': projects,
        'testimonials': testimonials,
        'services': services,
        'partners': partners,
        'awards': awards

    }

    return render(request, 'nimuit/nimuit.html', context)


def contact(request):

    if request.method == 'POST':
        
        contact_form = ContactForm(request.POST)
        
        
        if contact_form.is_valid():
            
            contact_form.save()
            messages.success(request, 'We will contact you soon.')
            # redirect to a new URL:
            return HttpResponseRedirect('/')
        
        
        
        
    
    
    # if a GET (or any other method) we'll create a blank form
    else:
        contact_form = ContactForm()
        
    
    context = {

    }

    return render(request, 'nimuit/nimuit.html', context)

def itsolution(request):

    context = {

    }

    return render(request, 'nimuit/it-solution.html', context)


def search(request):
    
    queryset1 = Project.objects.all()
    queryset2 = Service.objects.all()
    queryset3 = Expert.objects.all()
    
    query = request.GET.get('q')
    
    if query:
        queryset1 = queryset1.filter(
            Q(title__icontains=query) | Q(short_description__icontains=query)


        ).distinct()

        queryset2 = queryset2.filter(
            Q(title__icontains=query) | Q(short_description__icontains=query)


        ).distinct()

        queryset3 = queryset3.filter(
            Q(title__icontains=query) | Q(designation__icontains=query)


        ).distinct()
        
        
    
    
    context = {
        'queryset1': queryset1,
        'queryset2': queryset2,
        'queryset3': queryset3,

       
        'query': query


    }
    return render(request, 'nimuit/search.html', context)

