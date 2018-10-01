from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('compare/',views.compare,name='compare'),
    path('result/',views.result,name='result'),
]