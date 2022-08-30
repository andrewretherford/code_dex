from django.views.generic import TemplateView, DetailView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.dispatch import receiver

from .models import *
from .forms import UploadForm

# Create your views here.
class Landing(TemplateView):
   template_name = 'code_dex/landing.html'

class Home(TemplateView):
   template_name = 'code_dex/home.html'

   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['categories'] = Category.objects.filter(owner=self.request.user)
      category = self.request.GET.get('category')
      if category != None and category != 'all':
         context['records'] = Record.objects.filter(category=category, owner=self.request.user)
         context['header'] = Category.objects.get(id=category)
      else:
         context['records'] = Record.objects.filter(owner=self.request.user)
         context['header'] = 'All Records'
      return context

class Categories(TemplateView):
   template_name = 'code_dex/categories.html'

   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['categories'] = Category.objects.filter(owner=self.request.user)
      return context

class CreateCategory(CreateView):
   model = Category
   fields = ['name']

   def form_valid(self, form):
      form.instance.owner = self.request.user
      return super(CreateCategory, self).form_valid(form)

   def get_success_url(self):
      return reverse('home')

class CategoryUpdate(UpdateView):
   model = Category
   fields = ['name']
   success_url = '/categories'

class CategoryDelete(DeleteView):
   model = Category
   success_url = '/categories'

class Upload(CreateView):
   model = Record
   fields = ['title', 'category', 'file']
   template_name = 'code_dex/upload.html'

   def get_form(self, *args, **kwargs):
      form = super().get_form(*args, **kwargs)
      form.fields['category'].queryset = Category.objects.filter(owner=self.request.user)
      return form

   def form_valid(self, form):
      form.instance.owner = self.request.user
      return super(Upload, self).form_valid(form)

   def get_success_url(self):
      return reverse('record_detail', kwargs={'pk': self.object.pk})

class RecordDetail(DetailView):
   model = Record

class RecordUpdate(UpdateView):
   model = Record
   fields = ['title', 'category']

   def get_form(self, *args, **kwargs):
      form = super().get_form(*args, **kwargs)
      form.fields['category'].queryset = Category.objects.filter(owner=self.request.user)
      return form

   def get_success_url(self):
      next = self.request.POST.get('next', '/')
      return next

class RecordDelete(DeleteView):
   model = Record

   @receiver(models.signals.post_delete, sender=Record)
   def delete_from_s3(sender, instance, using, **kwargs):
      instance.file.delete(save=False)

   def get_success_url(self):
      next = self.request.POST.get('next', '/')
      return next

class ProfileEdit(UpdateView):
   model = User
   fields = ['username', 'email']
   template_name = 'code_dex/profile.html'
   success_url = '/home'

   def form_valid(self, form):
      return super().form_valid(form)

class Signup(View):
   def get(self, request):
      form = UserCreationForm()
      context = {"form": form}
      return render(request, 'registration/signup.html', context)

   def post(self, request):
      form = UserCreationForm(request.POST)
      if form.is_valid():
         user = form.save()
         login(request, user)
         return redirect('home')
      else:
         context = {"form": form}
         return render(request, 'registration/signup.html', context)