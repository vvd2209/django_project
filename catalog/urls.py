
from django.urls import path

from catalog.views import main_page, contacts

# � �������� ����� urls.py, ������� ��������� � ���������� � ����������� �������, ����������
# ������� ����� �������, �� ������ ����������� ������� ����������� ������� include.
# ��� ���� � ���������� catalog ������ ��������� ���� urls.py,
# � ��� � �� ����� ��������� ����������� ��������
urlpatterns = [
    path('', main_page),
    path('contacts/', contacts)
]