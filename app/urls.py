from django.urls import path
from .views import HomePageView, AboutPageView, BlotterPageView, AddPageView, EditPageView, DeletePageView, signup, login_view, logout_view

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('list/', BlotterPageView.as_view(), name='list'),
    path('add/', AddPageView.as_view(), name='add'),
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('add/', AddPageView.as_view(), name='add'),
    path('edit/<int:pk>/', EditPageView.as_view(), name='edit'),
    path('delete/<int:pk>/', DeletePageView.as_view(), name='delete'),
]