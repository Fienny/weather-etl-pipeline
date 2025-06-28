import json
import sqlite3
import os
from datetime import datetime

# Пути
DATA_DIR = "data"
DB_PATH = "weather.db"

def main():
    # Получаем последний JSON-файл
    files = [f for f in os.listdir(DATA_DIR) if f.endswith(".json")]
    latest_file = sorted(files)[-1]
    file_path = os.path.join(DATA_DIR, latest_file)

    # Загружаем данные
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Извлекаем нужные данные
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    city = data["name"]
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    weather = data["weather"][0]["description"]
    wind_speed = data["wind"]["speed"]

    # Подключаемся к базе
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Создаём таблицу, если не существует
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS weather (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            city TEXT,
            temperature REAL,
            humidity INTEGER,
            weather TEXT,
            wind_speed REAL
        )
    """)

    # Вставляем данные
    cursor.execute("""
        INSERT INTO weather (timestamp, city, temperature, humidity, weather, wind_speed)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (timestamp, city, temp, humidity, weather, wind_speed))

    # Сохраняем и закрываем
    conn.commit()
    conn.close()

    print(f"✔ Данные из {latest_file} добавлены в базу {DB_PATH}")

if __name__ == "__main__":
    main()