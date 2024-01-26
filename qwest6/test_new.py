import requests
from bs4 import BeautifulSoup

# URL сайта для парсинга
url = 'https://autoplaza51.ru/'

# Отправка GET-запроса к сайту
response = requests.get(url)

# Проверка успешности запроса
if response.status_code == 200:
    # Использование BeautifulSoup для парсинга HTML-кода страницы
    soup = BeautifulSoup(response.text, 'html.parser')

    # Находим и удаляем элемент с id="security"
    security_input = soup.find('input', {'id': 'security'})
    if security_input:
        security_input.extract()  # Используйте decompose() вместо extract(), если нужно удалить окончательно

    with open('../qwest5/new.html', 'w', encoding='utf-8') as file:
        file_new_content = file.write(soup.prettify())
        file.close()

    with open('../qwest5/new.html', 'r', encoding='utf-8') as file:
        file_content1 = file.read()
        file.close()

    # print(str(soup))
    # Запись обновленного содержимого soup в файл
    with open('../qwest5/output_modified.html', 'r', encoding='utf-8') as file:
        file_content = file.read()
        file.close()

    if file_content1 == file_content:
        print("Содержимое переменной soup и содержимое файла output.html идентичны.")
    else:
        print("Содержимое переменной soup и содержимое файла output.html различны.")

else:
    print(f'Ошибка при запросе: {response.status_code}')


