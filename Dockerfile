# syntax=docker/dockerfile:1
FROM python:3.11-slim

# Trabajaremos dentro de /app
WORKDIR /app

# Dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia TODO el contenido de la carpeta app/ a /app (incluye main.py, data.py, templates si los usas)
COPY app/ .

ENV PYTHONUNBUFFERED=1
EXPOSE 5000

# Lanza tu app (main.py está dentro de /app tras el COPY anterior)
CMD ["python", "main.py"]
