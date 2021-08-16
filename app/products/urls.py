from django.urls import path
from . import views

app_name = "products"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("products", views.ProductListView.as_view(), name="product-list"),
    path("<slug:slug>", views.ProductDetailView.as_view(), name="product-detail"),
]
