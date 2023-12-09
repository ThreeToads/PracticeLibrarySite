from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Author(models.Model):
    name_author = models.CharField(max_length=100)
    data_of_birth = models.DateField(null=True, blank=True)
    info_about_author = models.TextField(max_length=1000)
    slug = models.SlugField(max_length=255, unique=True, verbose_name='URL')

    def __str__(self):
        return self.name_author

    def get_absolute_url(self):
        return reverse('author', kwargs={'post_slug': self.slug})


class Books(models.Model):
    name = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    slug = models.SlugField(max_length=255, unique=True, verbose_name='URL')
    year_publish = models.IntegerField(default=0)
    short_info = models.TextField(max_length=2000)
    image_book = models.ImageField(upload_to='media/images/')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('book', kwargs={'book_slug': self.slug})

    class Meta:
        verbose_name = 'Список книг'
        verbose_name_plural = 'Список книг'
        ordering = ['name', 'author']


class Comment(models.Model):
    post = models.ForeignKey(Books,on_delete=models.SET_DEFAULT, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField(max_length=2000)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Комментарии'
        verbose_name_plural = 'Комментарии'
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)
