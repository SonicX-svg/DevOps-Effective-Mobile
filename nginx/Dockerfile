ARG NGINX_VERSION
FROM nginx:${NGINX_VERSION}

RUN mkdir -p /var/run \
    && chown -R nginx:nginx /var/run
    
# Устанавливаем curl для healthcheck (один пакет, без лишнего мусора) 
RUN apk add --no-cache curl

RUN mkdir -p /var/cache/nginx \
    && chown -R nginx:nginx /var/cache/nginx \
    && chown -R nginx:nginx /var/log/nginx \
    && chown -R nginx:nginx /etc/nginx/conf.d

RUN mkdir -p /var/run/nginx && chown -R nginx:nginx /var/run/nginx

RUN chown -R nginx:nginx /var/run /var/cache/nginx /var/log/nginx

USER nginx

COPY nginx.conf /etc/nginx/conf.d/default.conf

CMD ["nginx", "-g", "daemon off;"]
