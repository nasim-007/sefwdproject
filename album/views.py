from django.shortcuts import render
from album.forms import AddForm
from django.shortcuts import get_object_or_404
from bootstrap.views import AddAlbum
from .models import Carousel
from django.views.generic import CreateView, DeleteView, UpdateView
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin


class AlbumCreate(LoginRequiredMixin, CreateView):

    model = Carousel
    form_class = AddForm
    template_name = 'album/create.html'
    success_url = '/album'


class Delete(DeleteView):
    template_name = 'album/delete.html'

    def get_object(self):

        id = self.kwargs.get("id")
        return get_object_or_404(Carousel, id=id)

    def get_success_url(self):
        return reverse('album:index')


class Update(UpdateView):
    
    template_name = 'album/update.html'
    form_class = AddForm
    
    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Carousel, id=id)
    
    def get_success_url(self):
        return reverse('album:index')



def index(request):

    carousel_data = Carousel.objects.all()

    context = {

        'carousel_data': carousel_data

    }

    return render(request, 'album/index.html', context)