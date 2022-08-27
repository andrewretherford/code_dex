from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
   path('', views.Landing.as_view(), name='landing'),
   path('home/', login_required(views.Home.as_view()), name='home'),
   path('upload/', login_required(views.Upload.as_view()), name='upload'),
   path('settings/', login_required(views.Settings.as_view()), name='settings'),
   path('records-list/', login_required(views.RecordsList.as_view()), name='records_list'),
   path('records/<int:pk>', login_required(views.RecordDetail.as_view()), name='record_detail'),
   path('accounts/login/', views.Login.as_view(), name='login'),
   path('accounts/signup/', views.Signup.as_view(), name='signup'),
   path('accounts/logout/', views.Logout.as_view(), name='logout')
] 
