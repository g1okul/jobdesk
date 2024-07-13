"""
URL configuration for jet project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from zoro import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.show),
    path('home.html',views.show),
    path('about.html',views.show1),
    path('jobs.html',views.show2),
    path('view_job.html',views.show3),
    path('view_company.html',views.show4),
    path('contact.html',views.show5),
    path('login.html',views.show6),
    path('register.html',views.show7)

]
