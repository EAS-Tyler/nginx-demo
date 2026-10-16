# FROM nginx:stable-alpine3.24-slim
FROM nginx:latest
RUN apk upgrade --no-cache
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY html/index.html /usr/share/nginx/html/index.html

EXPOSE 80

USER nginx