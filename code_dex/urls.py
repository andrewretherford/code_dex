from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
   path('', views.Landing.as_view(), name='landing'),
   path('home/', views.Home.as_view(), name='home'),
   path('upload/', views.Upload.as_view(), name='upload'),
   path('settings/', views.Settings.as_view(), name='settings'),
   path('records-list/', views.RecordsList.as_view(), name='records_list'),
] 
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)