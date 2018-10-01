from django.urls import path,include
from . import views


urlpatterns = [
    path('signup_page/',views.signup_page,name='signup_page'),
    path('',views.Subscriber,name='Subscriber'),
    path('',include('django.contrib.auth.urls')),
    path('settings/',views.settings,name='settings'),
    path('settings/password/',views.password,name='password'),

]