import sqlite3
import matplotlib.pyplot as plt
from datetime import datetime

def main():
    DB_PATH = "weather.db"

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT timestamp, temperature FROM weather
        ORDER BY timestamp ASC
    """)
    rows = cursor.fetchall()
    conn.close()

    timestamps = [datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S") for row in rows]
    temperatures = [row[1] for row in rows]

    plt.figure(figsize=(10, 5))
    plt.plot(timestamps, temperatures, marker='o', color='orange')
    plt.title("📈 Температура во времени")
    plt.xlabel("Дата и время")
    plt.ylabel("Температура (°C)")
    plt.grid(True)
    plt.tight_layout()
    plt.xticks(rotation=45)

    # Автоматическое имя файла по дате-времени (опционально)
    timestamp_now = datetime.now().strftime("%Y-%m-%d_%H-%M")
    filename = f"data/temperature_plot_{timestamp_now}.png"

    # Или просто перезаписывай один файл:
    filename = "data/temperature_plot.png"

    plt.savefig(filename)
    plt.close()
    print(f"📊 График сохранён: {filename}")

if __name__ == "__main__":
    main()
