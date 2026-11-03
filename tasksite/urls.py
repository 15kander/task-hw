"""
URL configuration for tasksite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

import calculator
import orders.views
import students
from students import views
from calculator import views
from orders import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/', students.views.inp, name='inp'),
    path('student/result/', students.views.result, name='result'),
    path('calculator/', calculator.views.calc, name='calculator'),
    path('calculator/calcresult/', calculator.views.calcresult, name='calcresult'),
    path('order/', orders.views.getreq, name='order'),
    path('order/ordresult/', orders.views.ordresult, name='ordresult'),

]
