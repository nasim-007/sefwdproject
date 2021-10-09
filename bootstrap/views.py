from django.shortcuts import render
from .models import Corousel
from .forms import AlbumForm
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import CreateView, DeleteView, UpdateView

# Create your views here.

class AddAlbum(LoginRequiredMixin, CreateView):
    model = Corousel
    form_class = AlbumForm
    template_name = 'create.html'
    success_url = '/'

class Delete(DeleteView):
    template_name = 'delete.html'
    
    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Corousel, id=id)
    
    def get_success_url(self):
        return reverse('bootstrap:index')

class Update(UpdateView):
    
    template_name = 'update.html'
    form_class = AlbumForm
    
    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Corousel, id=id)
    
    def get_success_url(self):
        return reverse('bootstrap:index')



def index(request):

    carousel_data = Corousel.objects.all()

    context = {

        'carousel_data': carousel_data

    }

    return render(request, 'index.html', context)