from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404, request
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import *
from .models import *
from .utils import *


class LibraryHome(DataMixin, ListView):
    paginate_by = 2
    model = Books
    template_name = 'mainlibsite/index.html'
    context_object_name = 'books'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        return dict(list(context.items()) + list(c_def.items()))


def about(request):
    return render(request, 'mainlibsite/about.html', {'title': 'О сайте'})


class AddBook(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddBookForm
    template_name = 'mainlibsite/addbook.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Добавление книги')
        return dict(list(context.items()) + list(c_def.items()))


# def addbook(request):
#     if request.method == 'POST':
#         form = AddBookForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = AddBookForm()
#
#     return render(request, 'mainlibsite/addbook.html', {'form': form, 'menu': menu, 'title': 'Добавление книги'})


class ShowBook(DataMixin, DetailView):
    model = Books
    context_object_name = 'books'
    template_name = 'mainlibsite/books_vision.html'
    slug_url_kwarg = 'book_slug'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['books'])
        return dict(list(context.items()) + list(c_def.items()))


# def show_book(request, book_slug):
#     books = get_object_or_404(Books, slug=book_slug)
#     context = {
#         'books': books,
#         'menu': menu,
#         'title': 'Главная страница'
#     }
#
#     return render(request, 'mainlibsite/books_vision.html', context=context)


def login(request):
    return HttpResponse('Авторизация')


class RegisterUser(DataMixin, CreateView):
    form_class = UserCreationForm
    template_name = 'mainlibsite/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'mainlibsite/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизация')
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')


def pageNotFound(request, exception):
    return HttpResponseNotFound(f"<h1>Страница не найдена!</h1>")
