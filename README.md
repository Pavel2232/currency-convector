# 💶💱💴 Конвектор валют в реальном времени.
Тестовое задание для HR365
ЗЗадание:
Написать сервис "Конвертер валют" который работает по REST-API.
Пример запроса:
```http request
GET /api/rates?origin=USD&to=RUB&value=1
```
Ответ:
```json
{"Convert currency" : "95.9045400-RUB" }
```

Любой фреймворк в пределах python.
Данные о текущих курсах валют необходимо получать с внешнего сервиса.
Контейнерезация, документация.

- стек: FastApi, requests

## Как запустить:
* склонируйте репозиторий ``` git clone https://github.com/Pavel2232/currence-convector```
* Установите необходимые библиотеки  ```poetry install```
* заполните .env
- TOKEN_FIXER=[API_TOKEN](https://fixer.io/)

# Запуску через докер:
- ```docker build -t my_image_tag . ```
- ```docker run -p 80:80 — env_file .env my_image_tag  ```

# Для запуска программы без использования docker:
* ```uvicorn main:app --host 0.0.0.0 --port 80```

# Сервис доступен по GET запросу 
```http request
127.0.0.0/api/rates?origin=USD&to=RUB&value=1
```
- где origin валюта которую собираетесь перевести.
- to валюта в которую хотите перевести.
- количество валюты value
* Так же удобнее всего использовать это приложение [127.0.0.1/docs](127.0.0.1/docs) 
