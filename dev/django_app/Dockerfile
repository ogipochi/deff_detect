FROM python:3.6


RUN pip install django
RUN pip install pymysql
RUN mkdir -p /opt/services/django_app/src
WORKDIR /opt/services/django_app/src


EXPOSE 8000

ENTRYPOINT ["sh","test_startup.sh"]
