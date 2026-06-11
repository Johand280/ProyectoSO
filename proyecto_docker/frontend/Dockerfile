FROM rockylinux:9

RUN dnf install -y nginx && dnf clean all

COPY index.html /usr/share/nginx/html/index.html
COPY img /usr/share/nginx/html/img

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
