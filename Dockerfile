
FROM python:3.11

RUN pip install pytest

RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev

COPY . /app

WORKDIR /app

RUN pip install psycopg2

CMD ["python", "allure_db_script.py"]