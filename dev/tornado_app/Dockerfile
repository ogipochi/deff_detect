FROM python:3.7.2-stretch

RUN pip install tornado
RUN pip install pymysql
RUN pip install mojimoji
RUN pip install xlrd
RUN pip install pandas
RUN pip install numpy
RUN pip install openpyxl
WORKDIR /opt/services/tornado_app/src

ENTRYPOINT ["sh","startup.sh"]