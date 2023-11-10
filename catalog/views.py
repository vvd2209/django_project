from django.shortcuts import render

# Create your views here.

# Контроллер == функция def Contacts()
# Переменная request, где хранится инфа о том, что делал польз, откуда пришел и тд
def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'{name} ({email}): {message}')
    return render(request, 'catalog/contacts.html')

def main_page(request):
    return render(request, 'catalog/main_page.html')