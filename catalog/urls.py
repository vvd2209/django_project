
from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import (contacts, CategoryListView, ProductListView, ProductCreateView,
                           Main_pageListView, ProductDetailView, ProductUpdateView, ProductDeleteView)

# В корневом файле urls.py, который находится в директории с настройками проекта, необходимо
# описать новый маршрут, но вместо контроллера указать специальную функцию include.
# При этом в приложении catalog должен появиться файл urls.py,
# и уже в нём можно описывать необходимые маршруты

app_name = CatalogConfig.name

urlpatterns = [
    path('', Main_pageListView.as_view(), name='main_page'), # главная страница
    path('contacts/', contacts, name='contacts'), # контакты
    path('categories/', CategoryListView.as_view(), name='categories'), # все категории
    path('product/<int:pk>/', ProductListView.as_view(), name='products'), # все продукты категории
    path('view/<int:pk>/', ProductDetailView.as_view(), name='product_view'), # просмотр продукта
    path('create/', ProductCreateView.as_view(), name='product_create'), # добавление продукта
    path('edit/<int:pk>/', ProductUpdateView.as_view(), name='product_update'), # редактирование продукта
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'), # редактирование продукта
]