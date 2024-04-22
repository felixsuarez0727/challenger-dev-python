# Iimagen base oficial de Python
FROM python:3.11-slim

# Directorio de trabajo en el contenedor
WORKDIR /app

# Dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Resto del proyecto
COPY . .

WORKDIR /app/traffic_offenses

# Migrar la base de datos
RUN python manage.py makemigrations
RUN python manage.py migrate

# Exponer el puerto que usará Django
EXPOSE 8000

# Comando para ejecutar el servidor de desarrollo de Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
