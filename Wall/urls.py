# -*- coding:utf-8 -*- 
from django.conf.urls import url,include
from django.contrib import admin

from rest_framework import routers

from FundPart.forms import BootstrapAuthenticationForm
from FundPart import views
from FundPart.admin import *
from FundPart.FundPartUrls import *


from datetime import datetime

urlpatterns = [
    url(r'^admin/',include(admin.site.urls)),
    url(r'^fundpart/',include('FundPart.FundPartUrls')),
    url(r'^docs/',include('rest_framework_docs.urls')),
]

