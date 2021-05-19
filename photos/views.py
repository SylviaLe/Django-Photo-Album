from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, CreateView
from django.views.generic.edit import UpdateView
from .models import *

# Create your views here.
class GalleryView(ListView):
    template_name = 'gallery.html'
    categories = Category.objects.all()
    model = Photo
    context_object_name = 'photos'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = self.categories
        return context


#Photos views
class PhotosAddView(LoginRequiredMixin, CreateView):
    template_name = 'photo_new.html'
    model = Photo
    fields = ('name', 'description', 'category', 'image')

    # def form_valid(self, form): 
    #     form.instance.owner = self.request.user
    #     return super().form_valid(form)
    #https://docs.djangoproject.com/en/3.2/topics/class-based-views/intro/

class PhotosDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'photo_delete.html'
    context_object_name = 'photo'
    model = Photo
    login_url = 'login'
    success_url = reverse_lazy('gallery')

class PhotosEditView(LoginRequiredMixin, UpdateView):
    model = Photo
    fields = ('name', 'description', 'category')
    template_name = 'photo_edit.html'

class PhotosDetailView(DetailView):
    model = Photo
    template_name = 'photo_detail.html'
    context_object_name = 'photo'

#Category views

class CategoryDetailView(DetailView):
    template_name = 'category_detail.html'
    context_object_name = 'cate'
    categories = Category.objects.all()
    model = Category
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = self.categories
        return context


class CategoryAddView(LoginRequiredMixin, CreateView):
    template_name = 'category_new.html'
    model = Category
    fields = ('name',)
    # https://www.youtube.com/watch?v=OduVfuv44K8

    def get_success_url(self):
        return reverse_lazy('gallery')



####THE FUNCTION BASED VIEWS VERSION: https://github.com/divanov11/photo-album-app/blob/master/photos/views.py
