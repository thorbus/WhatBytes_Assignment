from django.contrib import admin
from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile/', user_views.profile, name='profile'),
    path('signup/', user_views.signup, name='signup'),
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('home/', user_views.home, name='home'),  # Home view
    path('password-reset-success/', user_views.password_reset_success, name='password_reset_success'),
    
    # Use reverse_lazy to ensure the URL is resolved correctly
    path('password-reset/', auth_views.PasswordChangeView.as_view(
        template_name='password_reset.html',
        success_url=reverse_lazy('password_reset_success')),  # Correct success URL
        name='password_reset'
    ),
]