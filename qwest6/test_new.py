import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText

def send_email(subject, body):
    # Your Gmail credentials
    gmail_user = 'kulikov51@gmail.com'
    gmail_password = ''

    # Recipient email address
    to = 'vanaws51@gmail.com'

    # Set up the MIMEText object
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = gmail_user
    msg['To'] = to

    # Establish a secure connection with the SMTP server
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(gmail_user, gmail_password)
        server.sendmail(gmail_user, to, msg.as_string())

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

    with open('new.html', 'w', encoding='utf-8') as file:
        file_new_content = file.write(soup.prettify())
        file.close()

    with open('new.html', 'r', encoding='utf-8') as file:
        file_content1 = file.read()
        file.close()

    with open('output_modified.html', 'r', encoding='utf-8') as file:
        file_content = file.read()
        file.close()

    if file_content1 == file_content:
        print("Содержимое переменной soup и содержимое файла output.html идентичны.")
    else:
        print("Содержимое переменной soup и содержимое файла output.html различны.")
        # Отправить уведомление по электронной почте
        subject = 'Уведомление: autoplaza51.ru'
        body = 'Содержимое переменной soup и содержимое файла output.html различны.'
        send_email(subject, body)
else:
    print(f'Ошибка при запросе: {response.status_code}')
    # Отправить уведомление по электронной почте
    subject = 'Уведомление: autoplaza51.ru'
    body = f'Ошибка при запросе: {response.status_code}'
    send_email(subject, body)
