FROM node:latest as node
RUN npm install -g @angular/cli
COPY ./app-frontend /app
WORKDIR /app
RUN npm install
RUN npm run build --configuration=production
CMD ["ng", "serve", "--host", "0.0.0.0", "--configuration", "production", "--live-reload", "false", "--disable-host-check", "true"]
