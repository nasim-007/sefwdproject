from django.shortcuts import render
from .models import Corousel
# Create your views here.

def index(request):

    carousel_data = Corousel.objects.all()

    context = {

        'carousel_data': carousel_data

    }

    return render(request, 'index.html', context)