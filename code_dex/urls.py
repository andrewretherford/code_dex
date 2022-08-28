from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
   path('', views.Landing.as_view(), name='landing'),
   path('home/', login_required(views.Home.as_view()), name='home'),
   path('upload/', login_required(views.Upload.as_view()), name='upload'),
   path('settings/', login_required(views.Settings.as_view()), name='settings'),
   path('categories/', login_required(views.Categories.as_view()), name='categories'),
   path('categories/create', login_required(views.CreateCategory.as_view()), name='category_create'),
   path('categories/<int:pk>/edit', login_required(views.CategoryUpdate.as_view()), name='category_update'),
   path('categories/<int:pk>/delete', login_required(views.CategoryDelete.as_view()), name='category_delete'),
   path('records/<int:pk>', login_required(views.RecordDetail.as_view()), name='record_detail'),
   path('records/<int:pk>/edit', login_required(views.RecordUpdate.as_view()), name='record_update'),
   path('records/<int:pk>/delete', login_required(views.RecordDelete.as_view()), name='record_delete'),
   path('accounts/login/', views.Login.as_view(), name='login'),
   path('accounts/signup/', views.Signup.as_view(), name='signup'),
   path('accounts/logout/', views.Logout.as_view(), name='logout')
] 
