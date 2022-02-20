from django.contrib import admin
from django.urls import path

from LibraryProject.library_app.views import home, book_add, book_edit, book_details, profile_details, profile_edit, \
    profile_delete, book_delete

urlpatterns = [
    path('', home, name='home'),
    path('add/', book_add, name='book add'),
    path('edit/<int:pk>/', book_edit, name='book edit'),
    path('details/<int:pk>/', book_details, name='book details'),
    path('delete/<int:pk>/', book_delete, name='book delete'),
    path('profile/', profile_details, name='profile details'),
    path('profile/edit/', profile_edit, name='profile edit'),
    path('profile/delete/', profile_delete, name='profile delete'),

]
