"""reestrdoma URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import re_path

from reestrdoma_app.controllers import house_controller, order_controller, user_controller

urlpatterns = [
    re_path(r'^houses/$', house_controller.HouseView.as_view()),
    re_path(r'^orders/$', order_controller.OrderView.as_view()),
    re_path(r'^profile/$', user_controller.ProfileView.as_view()),

    re_path(r'^register/$', user_controller.RegisterView.as_view()),
    re_path(r'^login/$', user_controller.LoginView.as_view()),

]
