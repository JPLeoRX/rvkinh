FROM node:latest as node
RUN npm install -g @angular/cli
COPY ./app /app
WORKDIR /app
RUN npm install
RUN ng build --prod
RUN chmod a+x main.sh
CMD './main.sh'