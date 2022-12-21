FROM python:3.9

ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip

COPY manage.py requirements.txt .env ./

RUN pip install -r requirements.txt

COPY . /purrfect_creations

WORKDIR /purrfect_creations

CMD ["python", "manage.py", "runserver"]
  