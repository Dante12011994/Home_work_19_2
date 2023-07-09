from django.shortcuts import render
import psycopg2


def main(request):
    """
    Переходит на страницу "Главная"
    """
    return render(request, 'catalog/main.html')


def contact(request):
    """
    Обрабатывает действия на странице "Контакты"
    """
    # Принимает информацию сообщения оставленого пользователем
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        text = request.POST.get('massage')

        # Записывает Сообщение оставленое пользователем в базу данных
        with psycopg2.connect(host="localhost", database='Django_work', user="postgres",
                              password="pecheneg762") as conn:
            with conn.cursor() as cur:
                cur.execute('INSERT INTO massage (first_name, email, title) VALUES (%s, %s, %s)',
                            (name, email, text))
        conn.close()

        # Воводит сообщение в консоль
        print(f'{name} ({email}): {text}')
    return render(request, 'catalog/contact.html')
