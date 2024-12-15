
# Library Service FastAPI

*Для использования API установите на компьютер Docker-Desktop
*Скачайте архив с приложением и распакуйте его
*Используя командную строку перейдите в корень каталога, например: `cd C:\library_service_FastAPI-main`
*Запустите контейнеры с помощью: `docker compose up -d --build`
(запросы адаптированы для использования их в ОС Windows)



## Author Use Cases

| Метод  | Описание                                | Пример запроса                                                                                                                  |
|--------|-----------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| POST   | Добавление нового автора                | `curl -X POST -H "Content-Type: application/json" -d "{\"first_name\": \"Лев\", \"last_name\": \"Толстой\", \"birth_date\": \"1828-09-09\"}" http://127.0.0.1/authors/` |
| GET    | Получение списка всех авторов           | `curl http://127.0.0.1/authors/`                                                                                             |
| GET    | Получение одного автора по ID           | `curl http://127.0.0.1/authors/1`                                                                                             |
| PUT    | Изменение всех характеристик автора     | `curl -X PUT -H "Content-Type: application/json" -d "{\"first_name\": \"Кристина\", \"last_name\": \"Агата\", \"birth_date\": \"1890-01-15\"}" http://127.0.0.1/authors/1` |
| PUT    | Изменение одной характеристики автора   | `curl -X PUT -H "Content-Type: application/json" -d "{\"first_name\": \"Кристи\"}" http://127.0.0.1/authors/1`               |
| DELETE | Удаление автора                         | `curl -X DELETE http://127.0.0.1/authors/1`                                                                                    |



## Book Use Cases
| Метод  | Описание                                | Пример запроса                                                                                                                  |
|--------|-----------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| POST   | Добавление новой книги                  | `curl -X POST -H "Content-Type: application/json" -d "{\"title\": \"Война и мир\", \"description\": \"Роман\", \"author_id\": 1}" http://127.0.0.1/books/` |
| GET    | Получение списка всех книг              | `curl http://127.0.0.1/books/`                                                                                             |
| GET    | Получение одной книги по ID             | `curl http://127.0.0.1/books/1`                                                                                             |
| PUT    | Изменение всех характеристик книги      | `curl -X PUT -H "Content-Type: application/json" -d "{\"title\": \"Грешница\", \"description\": \"Поэма\"}" http://127.0.0.1/books/1` |
| PUT    | Изменение одной характеристики книги    | `curl -X PUT -H "Content-Type: application/json" -d "{\"title\": \"Иоанн Дамаскин\"}" http://127.0.0.1/books/1`               |
| DELETE | Удаление книги                          | `curl -X DELETE http://127.0.0.1/books/1`                                                                                    |


## Borrow Use Cases
| Метод  | Описание                                | Пример запроса                                                                                                                  |
|--------|-----------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| POST   | Создание новой выдачи с датой           | `curl -X POST -H "Content-Type: application/json" -d "{\"book_id\": \"1\", \"reader_name\": \"Иван Иванов\", \"borrow_date\": \"2023-10-01\"}" http://127.0.0.1/borrows/` |
| POST   | Создание новой выдачи без даты(сегодня) | `curl -X POST -H "Content-Type: application/json" -d "{\"book_id\": \"1\", \"reader_name\": \"Иван Иванов\"}" http://127.0.0.1/borrows/` |
| GET    | Получение списка всех выдач             | `curl http://127.0.0.1/borrows/`                                                                                             |
| GET    | Получение одной выдачи по ID            | `curl http://127.0.0.1/borrows/1`                                                                                             |
| PATCH  | Возвращние книги без даты(сегодня)      | `curl -X PATCH -H "Content-Type: application/json" http://127.0.0.1/borrows/5/return` |
| PATCH  | Возвращние книги с датой                | `curl -X PATCH -H "Content-Type: application/json" -d "{\"return_date\": \"2024-12-22\"}" http://127.0.0.1/borrows/5/return`               |




