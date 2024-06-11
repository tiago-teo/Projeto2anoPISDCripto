FROM nginx:1.21.3-alpine

RUN rm /etc/nginx/conf.d/default.conf

COPY nginx.conf /etc/nginx/conf.d

RUN mkdir /usr/share/nginx/static

RUN mkdir /etc/nginx/snippets/

COPY self-signed.conf /etc/nginx/snippets/

COPY self-params.conf /etc/nginx/snippets/

COPY nginx-selfsigned.crt /etc/ssl/certs/

COPY dhparam.pem /etc/ssl/certs/

COPY nginx-selfsigned.key /etc/ssl/private/

#RUN nginx -t