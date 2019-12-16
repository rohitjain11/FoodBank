"""FoodBank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from mainapp import views
from ngo import views as nv
from donor import views as dv
from volunteer import views as vv

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page , name='home'),
    path('login_type/', views.logintype , name='logintype'),
    path('register_type/', views.registertype , name='registertype'),
    path('log_out/', views.logout , name='logout'),
    
    #ngo
    path('NGO_login/', nv.ngologin , name='ngologin'),
    path('NGO_register/', nv.ngoregister , name='ngoregister'),
    path('ngo_page/', nv.ngo , name='ngopage'),
   
    
    #donor
    path('donate/', dv.donate , name='donate'),
    path('donor_login', dv.dlogin , name='donorlogin'),
    path('donor_page/', dv.donor , name='donorpage'),
    path('donor_register/', dv.dregister , name='donorregister'),


    #volunteer
    path('volunteer_login/', vv.vlogin , name='volunteerlogin'),
    path('volunteer_register/', vv.vregister , name='volunteerregister'),
    path('volunteer_page/', vv.volunteer , name='volunteerpage'),
    path('accept/<int:id>', vv.accept , name='accept'),

]
