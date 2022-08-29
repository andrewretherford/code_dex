from django.urls import path
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
   path('', views.Landing.as_view(), name='landing'),
   # ---------------------------- AUTH URLS ----------------------------
   path('accounts/signup/', views.Signup.as_view(), name='signup'),
   path('profile/login', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
   path('profile/logout', login_required(auth_views.LogoutView.as_view(template_name='registration/logout.html')), name='logout'),
   path('profile/password', login_required(auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html')), name='password_change'),
   path('profile/password-changed', login_required(auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html')), name='password_change_done'),
   path('profile/edit/<int:pk>', login_required(views.ProfileEdit.as_view()), name='profile_edit'),
   # ---------------------------- SITE URLS ----------------------------
   path('home/', login_required(views.Home.as_view()), name='home'),
   path('upload/', login_required(views.Upload.as_view()), name='upload'),
   path('categories/', login_required(views.Categories.as_view()), name='categories'),
   path('categories/create', login_required(views.CreateCategory.as_view()), name='category_create'),
   path('categories/<int:pk>/edit', login_required(views.CategoryUpdate.as_view()), name='category_update'),
   path('categories/<int:pk>/delete', login_required(views.CategoryDelete.as_view()), name='category_delete'),
   path('records/<int:pk>', login_required(views.RecordDetail.as_view()), name='record_detail'),
   path('records/<int:pk>/edit', login_required(views.RecordUpdate.as_view()), name='record_update'),
   path('records/<int:pk>/delete', login_required(views.RecordDelete.as_view()), name='record_delete'),
] 
