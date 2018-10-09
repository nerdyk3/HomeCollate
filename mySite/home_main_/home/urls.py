from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('compare/',views.compare,name='compare'),
    path('result/',views.result,name='result'),
    path('about-us/',views.about_us,name='about_us'),
    path('FAQs/',views.faqs,name='faqs'),
    path('partner-with-us/',views.partner_with_us,name='partner_with_us'),
    path('privacy/',views.privacy,name='privacy'),
    path('T&C/',views.T_C,name='T_C'),
    path('why-us/',views.why_us,name='why_us'),
]