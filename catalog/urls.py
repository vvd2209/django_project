
from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import (contacts, CategoryListView, ProductListView, ProductCreateView,
                           MainPageListView, ProductDetailView, ProductUpdateView, ProductDeleteView)


app_name = CatalogConfig.name

urlpatterns = [
    path('', MainPageListView.as_view(), name='main_page'),
    path('contacts/', contacts, name='contacts'),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('product/<int:pk>/', ProductListView.as_view(), name='products'),
    path('view/<int:pk>/', ProductDetailView.as_view(), name='product_view'),
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('edit/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
]
