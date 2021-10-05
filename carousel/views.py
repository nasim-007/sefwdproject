from django.shortcuts import render
from .models import Carusel


def index(request):

    carousel = Carusel.objects.all()

    context = {

        'carousel': carousel

    }

    return render(request, 'carousel/index.html', context)