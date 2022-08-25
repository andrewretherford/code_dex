from django.views.generic import TemplateView, CreateView, ListView
from django.urls import reverse_lazy


from .models import Record
from .forms import UploadForm

# Create your views here.
class Landing(TemplateView):
   template_name = 'code_dex/landing.html'

class Home(TemplateView):
   template_name = 'code_dex/home.html'

class Upload(CreateView):
   model = Record
   form_class = UploadForm
   success_url = reverse_lazy('records_list')
   template_name = 'code_dex/upload.html'

class RecordsList(ListView):
   model = Record
   template_name = 'code_dex/record.html'

class Settings(TemplateView):
   template_name = 'code_dex/settings.html'

