FROM node:10-alpine

RUN mkdir -p /opt/services/react_app/src/front

COPY ./front /opt/services/react_app/src

WORKDIR /opt/services/react_app/src/front

RUN npm install

ENTRYPOINT ["sh","startup.sh"]