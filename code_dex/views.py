from django.views.generic import TemplateView, CreateView, ListView, DetailView, RedirectView, View
from django.urls import reverse
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render

from .models import *
from .forms import UploadForm

# Create your views here.
class Landing(TemplateView):
   template_name = 'code_dex/landing.html'

class Home(TemplateView):
   template_name = 'code_dex/home.html'

   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['categories'] = Category.objects.all()
      category = self.request.GET.get('category')
      if category != None and category != 'all':
         context['records'] = Record.objects.filter(category=category, owner=self.request.user)
         context['header'] = Category.objects.get(id=category)
      else:
         context['records'] = Record.objects.filter(owner=self.request.user)
         context['header'] = 'All Records'
      return context

class Upload(CreateView):
   model = Record
   fields = ['title', 'category', 'file']
   template_name = 'code_dex/upload.html'

   def form_valid(self, form):
      form.instance.owner = self.request.user
      return super(Upload, self).form_valid(form)

   def get_success_url(self):
      return reverse('record_detail', kwargs={'pk': self.object.pk})

class RecordsList(ListView):
   model = Record

   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      category = self.request.GET.get('category')
      print(category)


class RecordDetail(DetailView):
   model = Record

class Settings(TemplateView):
   template_name = 'code_dex/settings.html'

class Login(LoginView):
   template_name = 'registration/login.html'

class Logout(LogoutView):
   template_name = 'registration/logout.html'
   next_page = None

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