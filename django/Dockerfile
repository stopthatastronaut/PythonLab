FROM python:3.9.19-alpine3.20

WORKDIR /usr/src/app

COPY ./app/requirements.txt ./

RUN pip install -r requirements.txt

COPY ./app/ .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]