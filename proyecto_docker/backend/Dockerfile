FROM rockylinux:9

# Instalar Python 3
RUN dnf install -y python3 && dnf clean all

WORKDIR /app
COPY server.py .

# Exponer el puerto 5000 y arrancar el script con python3
EXPOSE 5000
CMD ["python3", "server.py"]
