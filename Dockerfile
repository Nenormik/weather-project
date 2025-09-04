# Используем официальный образ Python
FROM python:3.9-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файл зависимостей в контейнер
COPY requirements.txt ./

# Устанавливаем зависимости
RUN pip install -r requirements.txt

# Копируем код приложения в контейнер
COPY . .

# Запускаем приложение
CMD ["python3", "main.py"]

