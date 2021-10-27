from django.shortcuts import render
from .models import Expert, Project, Testimonial, Service, Partner, Award
from .forms import AppointmentForm
from django.http import HttpResponseRedirect
# Create your views here.

def index(request):

    experts = Expert.objects.all()
    projects = Project.objects.all()
    testimonials = Testimonial.objects.all()
    services = Service.objects.all()
    partners = Partner.objects.all()
    awards = Award.objects.all()
    
    if request.method == 'POST':
        
        appointment_form = AppointmentForm(request.POST)
        
        if appointment_form.is_valid():
            
            appointment_form.save()
            # redirect to a new URL:
            return HttpResponseRedirect(request.path_info)

    
    
    
    # if a GET (or any other method) we'll create a blank form
    else:
        
        appointment_form = AppointmentForm()
    
    
    context = {

        'experts': experts,
        'projects': projects,
        'testimonials': testimonials,
        'services': services,
        'partners': partners,
        'awards': awards

    }

    return render(request, 'nimuit/nimuit.html', context)