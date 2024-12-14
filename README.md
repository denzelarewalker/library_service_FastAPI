
# Library Service FastAPI


Запустите контейнеры с помощью: `docker-compose up -d` или `docker compose up -d --build`



| POST запрос для авторов |
|-|
| `curl -X POST -H "Content-Type: application/json" -d "{\"first_name\": \"Лев\", \"last_name\": \"Толстой\", \"birth_date\": \"1828-09-09\"}" http://127.0.0.1/authors/` |


| GET запросы для авторов |
|-|-|
| все авторы | один автор по id |
| `curl http://127.0.0.1/authors/` | `http://127.0.0.1/authors/1` |

| PUT запросы для авторов |
| изменение всех характеритик | изменение одной характеритики |
|-|-|
| `curl -X PUT -H "Content-Type: application/json" -d "{\"first_name\": \"Кристина\", \"last_name\": \"Агата\", \"birth_date\": \"1890-01-15\"}" http://127.0.0.1/authors/1` | `curl -X PUT -H "Content-Type: application/json" -d "{\"first_name\": \"Кристи\"}" http://127.0.0.1/authors/1` |


| DELETE запросы для авторов |
|-|
| `curl -X DELETE http://127.0.0.1/authors/1` |








--------------------------------------------GET----------------------------------------------------------
curl http://127.0.0.1/books/ 

http://127.0.0.1/books/1
--------------------------------------------POST----------------------------------------------------------
curl -X POST -H "Content-Type: application/json" -d "{\"title\": \"Война и мир\", \"description\": \"Роман\", \"author_id\": 1}" http://127.0.0.1/books/

curl -X POST -H "Content-Type: application/json" -d "{\"title\": \"Анна Каренина\", \"description\": \"Роман\", \"author_id\": 1}" http://127.0.0.1/books/

--------------------------------------------PUT----------------------------------------------------------

curl -X PUT -H "Content-Type: application/json" -d "{\"title\": \"ГРЕШНИЦА\", \"description\": \"Поэма\"}" http://127.0.0.1/books/3
--------------------------------------------DELETE----------------------------------------------------------
curl -X DELETE "Content-Type: application/json" http://127.0.0.1/books/1









--------------------------------------------GET----------------------------------------------------------
curl http://127.0.0.1/borrows/ 

http://127.0.0.1/borrows/1
--------------------------------------------POST----------------------------------------------------------
curl -X POST -H "Content-Type: application/json" -d "{\"book_id\": \"2\", \"reader_name\": \"Иван Иванов\", \"borrow_date\": \"2023-10-01\"}" http://127.0.0.1/borrows/

--------------------------------------------PUT----------------------------------------------------------

curl -X PUT -H "Content-Type: application/json" -d "{\"title\": \"ГРЕШНИЦА\", \"description\": \"Поэма\"}" http://127.0.0.1/books/3
--------------------------------------------DELETE----------------------------------------------------------
curl -X PATCH http://127.0.0.1/borrows/5/return -H 'Content-Type: application/json'
curl -X PATCH -H "Content-Type: application/json" -d http://127.0.0.1/borrows/5/return

curl -X PATCH -H "Content-Type: application/json" -d "{"return_date": \"2024-12-14\"}" http://127.0.0.1/borrows/5/return
