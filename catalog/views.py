from django.shortcuts import render


def main(request):
    return render(request, 'catalog/main.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        text = request.POST.get('massage')
        print(f'{name} ({email}): {text}')
    return render(request, 'catalog/contact.html')
