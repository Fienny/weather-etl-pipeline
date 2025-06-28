import sqlite3
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.dates as mdates
from datetime import datetime

def main():
    fig, ax = plt.subplots(figsize=(10, 5))
    line, = ax.plot([], [], marker='o', color='tomato')

    def get_data():
        conn = sqlite3.connect("weather.db")
        cursor = conn.cursor()
        cursor.execute("""
            SELECT timestamp, temperature FROM weather
            ORDER BY timestamp ASC
        """)
        rows = cursor.fetchall()
        conn.close()
        timestamps = [datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S") for row in rows]
        temperatures = [row[1] for row in rows]
        return timestamps, temperatures

    def animate(frame):
        x, y = get_data()
        line.set_data(x, y)

        ax.clear()
        ax.plot(x, y, marker='o', color='tomato')

        ax.set_title("🌡 Live-график температуры")
        ax.set_xlabel("Время")
        ax.set_ylabel("Температура (°C)")
        ax.grid(True)

        # ✅ Ось времени: красота!
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M\n%d-%m'))
        fig.autofmt_xdate(rotation=45)

        ax.relim()
        ax.autoscale_view()

        return line,

    ani = animation.FuncAnimation(
        fig, animate, interval=60_000
    )

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
