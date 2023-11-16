
from django.urls import path

from catalog.views import main_page, contacts

# В корневом файле urls.py, который находится в директории с настройками проекта, необходимо
# описать новый маршрут, но вместо контроллера указать специальную функцию include.
# При этом в приложении catalog должен появиться файл urls.py,
# и уже в нём можно описывать необходимые маршруты
urlpatterns = [
    path('', main_page),
    path('contacts/', contacts),
    path('')
]