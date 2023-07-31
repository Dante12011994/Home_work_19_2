from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView
from pytils.translit import slugify

from blog.models import Article


class BlogCreateView(CreateView):
    model = Article
    fields = ('title', 'body', 'preview',)
    success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()

        return super().form_valid(form)


class BlogListView(ListView):
    model = Article


class BlogUpdateView(UpdateView):
    model = Article
    fields = ('title', 'body', 'preview',)
    success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()

        return super().form_valid(form)


class BlogDetailView(DetailView):
    model = Article


class BlogDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('blog:list')
