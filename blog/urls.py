from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogCreateView, BlogListView, BlogDetailView, BlogUpdateView, BlogDeleteView, toggle_activity

app_name = BlogConfig.name


urlpatterns = [
    path('create/', BlogCreateView.as_view(), name='create'), # создать блог
    path('', BlogListView.as_view(), name='list'), # блоги списком
    path('view/<int:pk>/', BlogDetailView.as_view(), name='view'), # посмотреть блог
    path('edit/<int:pk>/', BlogUpdateView.as_view(), name='edit'), # редактировать блог
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='delete'), # удалить блог
    path('activity/<int:pk>/', toggle_activity, name='toggle_activity'), # активация/деактивация блога

]