from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.root_redirect, name='root_redirect'),  # Handles redirect based on auth status
    path('home/', views.home_view, name='home'),  # For logged-in students

    path('welcome/', views.public_home_view, name='public_home'),  # For anonymous users
    path('quiz/<str:topic>/', views.quiz_topic_view, name='quiz_topic'),

    # Auth
    path('signup/', views.register_student, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='public_home'), name='logout'),
]
