FROM nginx:1.27-alpine
RUN apk upgrade --no-cache 
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY html/index.html /usr/share/nginx/html/index.html

EXPOSE 80

USER nginx