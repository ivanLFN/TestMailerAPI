# Test Task - Mailer API

API представляет из себя тестовое задание компании "Фабрика решений". В нем реализованны следующие возможности:

1. Добавление, удаление, изменение клиентов в справочник со всеми атрибутами
2. Добавление, удаление, изменение рассылкок со всеми атрибутами
3. Получение общей статистики по созданным рассылкам и количеству отправленных сообщений по ним
4. Обработка активных рассылок и отправка сообщений клиентам
5. Рассылка клиентам происходит авитоматически, в зависимости от временного интервала рассылки.

## Системные требования

1. Python 3.8 или поздняя версия
2. Установленный менеджер пакетов pip

## Установка и запуск проекта

1. Клонируйте репозиторий на локальную машину: 
```git clone https://github.com/ivanLFN/TestMailerAPI.git```

2. Перейдите в каталог проекта:
```cd "newsletter"```

3. Установите зависимости: 
```pip install -r requirements.txt```

## Запуск проекта

1. Запустите сервер Django:
```python manage.py runserver```

2. Запустите файл планировщика задач из корневой деректории:
python scheduler.py

3. Проект будет доступен по адресу 
[http://localhost:8000/](http://localhost:8000/)


## Использование API

## Работа с клиентами:

1. Получение списка клиентов GET:
```http://localhost:8000/clients/```
Пример ответа content:
```
[
    {"id":3,"phone_number":"70000000000","operator_code":"913","tag":"new_client","timezone":"GMT+3"},
    {"id":4,"phone_number":"79131111111","operator_code":"913","tag":"non","timezone":"GMT+3"},
]
```
2. Создание нового клиента в словаре POST:
```http://localhost:8000/clients/```

Пример использования на python:

```url = 'http://127.0.0.1:8000/clients/'
data = {
    "phone_number": "90000000000",
    "operator_code": "913",
    "tag": "new_client",
    "timezone": "GMT+3"
}
headers = {'Content-Type': 'application/json'}
response = requests.post(url, data=json.dumps(data), headers=headers)
print(response.text)
```

Запрос возвращает 200 и нового клиента (responce.text), либо ошибку 40X:
```{"id":8,"phone_number":"90000000000","operator_code":"913","tag":"new_client","timezone":"GMT+3"}```

3. Получение, обновление и удаление информации о клиенте по его идентификатору:
```http://localhost:8000/clients/<int:pk>/```

GET:
Получаем информацию о клиенте (content)
Пример:
```http://localhost:8000/clients/4```
Ответ (content):
```{"id":4,"phone_number":"79131111111","operator_code":"913","tag":"non","timezone":"GMT+3"}```

4. PUT ```/clients/<int:pk>/```: Обновляет данные конкретного клиента (Client) с указанным идентификатором (pk).

5. DELETE ```/clients/<int:pk>/```: Удаляет конкретного клиента (Client) с указанным идентификатором (pk).

## Работа с рассылками:

1. ```GET /mailings/```: Возвращает список всех рассылок (Mailing) с их данными.

2. ```POST /mailings/```: Создает новую рассылку (Mailing) на основе предоставленных данных.

Пример использования на python:

```
url = 'http://127.0.0.1:8000/mailings/' 
data = {
    "start_datetime": "2023-05-18T09:00:00",
    "message_text": "Third mailing!",
    "filter_operator_code": "913",
    "filter_tag": "new_client",
    "end_datetime": "2023-05-25T18:00:00"
}
headers = {'Content-Type': 'application/json'}
response = requests.post(url, data=json.dumps(data), headers=headers)
```
3. GET ```/mailings/<int:pk>/```: Возвращает данные конкретной рассылки (Mailing) с указанным идентификатором (pk).

4. PUT ```/mailings/<int:pk>/```: Обновляет данные конкретной рассылки (Mailing) с указанным идентификатором (pk).

5. DELETE ```/mailings/<int:pk>/```: Удаляет конкретную рассылку (Mailing) с указанным идентификатором (pk).


## Работа с сообщениями:

1. GET ```/messages/```: Возвращает список всех сообщений (Message) с их данными.

2. POST ```/messages/```: Создает новое сообщение (Message) на основе предоставленных данных.

Пример использования на python:

```
url = 'http://127.0.0.1:8000/messages/' 
data = {
    "created_at": "2023-05-18T09:00:00",
    "status": "Отправлено",
    "mailing": "1",
    "client": "1"
}
headers = {'Content-Type': 'application/json'}
response = requests.post(url, data=json.dumps(data), headers=headers)
```

3. GET ```/messages/<int:pk>/```: Возвращает данные конкретного сообщения (Message) с указанным идентификатором (pk).

4. PUT ```/messages/<int:pk>/```: Обновляет данные конкретного сообщения (Message) с указанным идентификатором (pk).

5. DELETE ```/messages/<int:pk>/```: Удаляет конкретное сообщение (Message) с указанным идентификатором (pk).


## Получение статистики рассылки:

1. GET ```/mailings/<int:pk>/statistics/```: Возвращает статистику рассылки (Mailing) с указанным идентификатором (pk), включая данные о сообщениях.


## Запуск возможных рассылок:

1. GET ```/activate_mailing/```: Выполняет активацию рассылки. Внутри этой функции происходит создание экземпляра Mailer и вызов метода process_active_mailings(), который обрабатывает активные рассылки. Также возвращает статистику рассылки в виде JSON-ответа.