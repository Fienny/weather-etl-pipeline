import sqlite3

DB_PATH = "weather.db"

def main():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    print("📊 Анализ погоды по базе данных:\n")

    # 1. Количество записей
    cursor.execute("SELECT COUNT(*) FROM weather")
    print(f"Количество записей: {cursor.fetchone()[0]}")

    # 2. Средняя температура
    cursor.execute("SELECT ROUND(AVG(temperature), 2) FROM weather")
    print(f"Средняя температура: {cursor.fetchone()[0]}°C")

    # 3. Самая высокая температура
    cursor.execute("SELECT MAX(temperature), timestamp FROM weather")
    max_temp, timestamp = cursor.fetchone()
    print(f"Макс. температура: {max_temp}°C ({timestamp})")

    # 4. Погода по частоте
    cursor.execute("""
        SELECT weather, COUNT(*) as count
        FROM weather
        GROUP BY weather
        ORDER BY count DESC
    """)
    print("\nЧастота погодных условий:")
    for row in cursor.fetchall():
        print(f"— {row[0]}: {row[1]} раз")

    conn.close()

if __name__=="__main__":
    main()