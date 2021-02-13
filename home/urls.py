from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.home, name="Home"),
    path('about', views.about, name="About"),
    path('contact', views.contact, name="Contact"),
    path('search', views.search, name="Search"),
    path('login', views.handleLogin, name="Login"),
    path('signup', views.signup, name="Sign Up"),
    path('logout', views.handleLogout, name="LogOut"),
]
