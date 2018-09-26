from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index),
    path('compare/',views.compare,name='compare')
]