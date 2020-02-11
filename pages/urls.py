from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('tos/', views.TosPageView.as_view(), name='tos'),
    path('about/', views.AboutPageView.as_view(), name='about'),
    path('faq/', views.FaqPageView.as_view(), name='faq'),
]

