FROM python:3.8.8

WORKDIR /home/

RUN git clone https://github.com/Hwnagseunghwan/2793design.git

WORKDIR /home/2793design/

RUN pip install -r requirements.txt

RUN echo "SECRET_KEY=django-insecure-l!kzqi(2^su7zt3e@g8!yt$#70ez0bw$_u#c*h+)(c&go^vv_b" > .env

RUN python manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]