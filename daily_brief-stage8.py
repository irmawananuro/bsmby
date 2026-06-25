# === Stage 8: Реализуй текстовый интерфейс команд с меню действий ===
# Project: DailyBrief
def show_menu():
    print("\n=== DailyBrief Меню ===")
    print("1. Показать задачи дня")
    print("2. Добавить новую задачу")
    print("3. Просмотреть заметки")
    print("4. Отметить событие как завершённое")
    print("5. Вывести итоги дня")
    print("6. Сохранить и выйти")
    try:
        choice = input("Выберите действие (1-6): ").strip()
        if choice == "1":
            tasks = get_tasks_for_today()
            display_list(tasks, "Задачи на сегодня")
        elif choice == "2":
            task_text = input("Введите текст задачи: ")
            priority = input("Приоритет (низкий/средний/высокий): ").lower()
            add_task(task_text, priority)
            print("Задача добавлена.")
        elif choice == "3":
            notes = get_notes()
            display_list(notes, "Заметки")
        elif choice == "4":
            event_id = input("ID события для завершения: ")
            mark_event_complete(event_id)
        elif choice == "5":
            show_daily_summary()
        elif choice == "6":
            save_data()
            print("Данные сохранены. До свидания!")
            exit(0)
        else:
            print("Неверный выбор.")
    except KeyboardInterrupt:
        print("\nВыход из программы.")
