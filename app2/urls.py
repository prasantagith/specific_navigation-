from django.urls import path
from app2.views import *

app_name='prasanta'
urlpatterns = [
    path('page/',page,name='page'),
]