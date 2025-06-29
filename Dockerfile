FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt ./

RUN apt-get update && apt-get install -y unixodbc

RUN pip install --no-cache-dir -r requirements.txt

COPY ./src/app ./src/app

CMD ["python", "./src/app/app.py"]
