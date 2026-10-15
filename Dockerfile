FROM nginx:stable-alpine

# Remove curl if it's present in the base image (it is preinstalled in some Nginx Alpine images)
RUN apk del --no-cache curl && apk upgrade --no-cache || apk upgrade --no-cache

COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY html/index.html /usr/share/nginx/html/index.html

EXPOSE 80

USER nginx