from django.shortcuts import render
from .models import Expert, Project, Testimonial
# Create your views here.
def index(request):

    experts = Expert.objects.all()
    projects = Project.objects.all()
    testimonials = Testimonial.objects.all()
    context = {

        'experts': experts,
        'projects': projects,
        'testimonials': testimonials

    }

    return render(request, 'nimuit/nimuit.html', context)