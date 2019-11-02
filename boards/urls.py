from django.urls import path, include
from . import views

urlpatterns = [
    #path('', views.board_list, name='board_list'),
    path('', views.boardhome, name='boardhome'),
    path('<int:pk>/', views.board_companies, name='board_companies'),
    path('<int:pk>/new/', views.new_company, name='new_company'),
    path('<int:pk>/companies/<int:company_pk>/', views.company_reviews, name='company_reviews'),
    path('<int:pk>/companies/<int:company_pk>/add_review/', views.add_review_company, name='add_review_company'),
    path('<int:pk>/companies/<int:company_pk>/reviews/<int:review_pk>/edit/', views.ReviewUpdateView.as_view(), name='edit_review'),
]
