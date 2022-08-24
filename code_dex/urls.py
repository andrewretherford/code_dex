from django.urls import path
from . import views

app_name = 'code_dex'
urlpatterns = [
   path('', views.Landing.as_view(), name='landing')
]