
FROM python:3.11

RUN pip install pytest

COPY . /app

WORKDIR /app

RUN pip install psycopg2

CMD ["python", "db_python_script.py"]