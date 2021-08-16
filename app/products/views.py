from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Product


class IndexView(TemplateView):
    template_name = "index.html"


class ProductListView(ListView):
    model = Product
    paginate_by = 10
    ordering = ["name"]

class ProductDetailView(DetailView):
    model = Product



