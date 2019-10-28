from django.urls import path, include
from . import views

urlpatterns = [
    #path('', views.board_list, name='board_list'),
    path('', views.boardhome, name='boardhome'),
    path('<int:pk>/', views.board_companies, name='board_companies'),
    path('<int:pk>/new/', views.new_company, name='new_company'),
]
