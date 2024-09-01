from django.urls import path
from accounts.views import *

urlpatterns=[
    path('',home,name='home'),
    path('add',add,name='add')
]