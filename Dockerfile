FROM python:3.13.0

ENV PYTHONBUFFERED 1

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

# Удаление файла
RUN rm .env

# Переименование файла
RUN mv .env_docker .env

EXPOSE 8001

CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]
