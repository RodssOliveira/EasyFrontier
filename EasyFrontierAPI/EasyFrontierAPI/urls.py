"""EasyFrontierAPI URL Configuration

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
from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('', views.main_render),
    path('admin/', admin.site.urls),

    path('order/', views.order_process),

    #API
    path('api/Remedio', views.medicines_all),
    path('api/Remedio/<str:med_name>', views.medicines),
    path('api/Remedio/<str:med_name>/<str:value>', views.medicines_specify),
    path('api/generate_order_code/', views.code_generator)
]
