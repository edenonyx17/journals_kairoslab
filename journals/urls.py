from django.urls import path
from .views import (
  journalListView,
  journalDetailView,
  journalCreateView,
  journalUpdateView,
  journalDeleteView
)




urlpatterns = [
    path('', journalListView.as_view(), name='home'),
    path('journals/<int:pk>/', journalDetailView.as_view(), name='journal-detail'),
    path('create/', journalCreateView.as_view(), name='create'),
    path('update/<int:pk>/', journalUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', journalDeleteView.as_view(), name='delete'),
]