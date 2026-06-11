FROM rockylinux:9

# Instalar Nginx y limpiar caché para reducir espacio
RUN dnf install -y nginx && dnf clean all

# Copiar tu archivo web al directorio por defecto de Nginx en Red Hat
COPY index.html /usr/share/nginx/html/index.html

# Exponer el puerto 80 y arrancar Nginx en primer plano
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
