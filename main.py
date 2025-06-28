import scripts.fetch_weather as fetch
import scripts.save_to_db as save
import scripts.analyze as analyze
import scripts.visualize as visualize
import scripts.animate as animate
import schedule
import time

def run_pipeline():
    print("\n🚀 [ETL] Запуск пайплайна...\n")
    fetch.main()
    save.main()
    analyze.main()
    visualize.main()
    print("✅ [ETL] Пайплайн завершён.\n")

def run_loop_mode():
    schedule.every(0.5).minutes.do(run_pipeline)  # можно .minutes для тестов
    print("⏳ Сервис запущен. Ожидаем расписания... (Ctrl+C для выхода)")
    run_pipeline()  # первый запуск вручную
    while True:
        schedule.run_pending()
        time.sleep(1)

def run_live_graph():
    print("📊 Запуск анимированного графика...")
    animate.main()

if __name__ == "__main__":
    print("""
🌦 WEATHER ETL — Выберите режим запуска:
1 — Один запуск ETL
2 — Автоматический запуск по расписанию
3 — Анимированный live-график
""")
    choice = input("Введите номер режима: ")

    if choice == "1":
        run_pipeline()
    elif choice == "2":
        run_loop_mode()
    elif choice == "3":
        run_live_graph()
    else:
        print("❌ Неверный выбор.")

