from django.urls import path
from .views import HomePageView, AboutPageView, BlotterPageView, AddPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('list/', BlotterPageView.as_view(), name='list'),
    path('add/', AddPageView.as_view(), name='add'),
]