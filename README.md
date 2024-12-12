poetry shell

uvicorn library_service.main:app --reload

uvicorn library_service.main_reserve:app --reload


poetry show


poetry add "fastapi[standard]"

fastapi dev library_service/main.py



3. Запуск контейнеров:

Сначала запустите контейнер PostgreSQL:

docker build -t fastapi-postgres-db -f Dockerfile.postgres .
docker run -d -p 5432:5432 --name fastapi-postgres fastapi-postgres-db


Затем постройте и запустите контейнер FastAPI: Замените `fastapi_app` на реальное имя вашей директории с приложением. В переменных окружения укажите параметры подключения к PostgreSQL:

docker build -t fastapi-app -f Dockerfile.fastapi fastapi_app
docker run -d -p 8000:8000 --name fastapi-container \
  -e DATABASE_URL="postgresql://fastapi_user:fastapi_password@fastapi-postgres:5432/fastapi_db" \
  fastapi-app





  Запустите контейнеры с помощью:

docker compose up -d --build

curl -X POST -H 'Content-Type: application/json' -d '{"name": "Лев Толстой", "birth_date": "1828-09-09T00:00:00", "books": ["Война и мир", "Анна Каренина"]}' http://127.0.0.1:8000/authors/

curl -X POST -H "Content-Type: application/json" -d "{\"name\":\"Лев Толстой\",\"surname\":\"Толстой\",\"birthdate\":\"1828-09-09\"}" http://127.0.0.1:8000/authors/
