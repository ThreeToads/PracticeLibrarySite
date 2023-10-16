from django.urls import path, re_path

from .views import *


urlpatterns = [
    path('', LibraryHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('addbook/', AddBook.as_view(), name='add_book'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', LoginUser.as_view(), name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('book/<slug:book_slug>/', ShowBook.as_view(), name='book'),

]
