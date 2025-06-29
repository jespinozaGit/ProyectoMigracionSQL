FROM python:3.10-slim

# Crear directorio de la app
WORKDIR /app

# Copiar requirements y los instala
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código
COPY . .

# Puerto en el que corre Flask
EXPOSE 8000

# Comando por defecto
CMD ["python", "app.py"]
