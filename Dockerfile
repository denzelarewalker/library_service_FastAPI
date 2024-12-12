FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN pip install poetry
RUN poetry config virtualenvs.create false 
RUN poetry install

COPY . .

#CMD ["uvicorn", "library_service.main:app", "--host", "0.0.0.0", "--port", "8000"]