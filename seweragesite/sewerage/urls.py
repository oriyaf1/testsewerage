from django.urls import path
from .views import (
    ControllerListView, 
    ControllerUpdateView, 
    ControllerDetailView, 
    ControllerCreateView,
    ControllerDeleteView
)
from . import views

urlpatterns = [
    path('', views.home, name='sewerage-home'),
    path('controller/<int:pk>/', ControllerDetailView.as_view(), name='controller-detail'),
    path('controller/new/', ControllerCreateView.as_view(), name='controller-create'),
    path('controller/<int:pk>/update', ControllerUpdateView.as_view(), name='controller-update'),
    path('controller/<int:pk>/delete', ControllerDeleteView.as_view(), name='controller-delete'),
    path('about/', views.about, name='sewerage-about'),
]