import requests
import json
import os
from dotenv import load_dotenv
from datetime import datetime

def main():
    # Загрузка переменных из .env
    load_dotenv()
    API_KEY = os.getenv("API_KEY")
    CITY = os.getenv("CITY")
    UNITS = os.getenv("UNITS", "metric")
    LANG = os.getenv("LANG", "en")

    # Формируем URL запроса
    url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units={UNITS}&lang={LANG}"

    # Выполняем запрос
    response = requests.get(url)
    data = response.json()

    # Проверяем статус
    if response.status_code == 200:
        # Сохраняем в JSON с таймстампом
        now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        os.makedirs("data", exist_ok=True)
        file_path = f"data/weather_{now}.json"
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"✔ Данные сохранены в {file_path}")
    else:
        print("❌ Ошибка при получении данных:", data)

if __name__=="__main__":
    main()