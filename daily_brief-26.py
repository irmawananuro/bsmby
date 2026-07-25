# === Stage 26: Добавь набор демо-команд для быстрого ручного тестирования ===
# Project: DailyBrief
def demo_commands():
    """Демо-команды для ручного тестирования DailyBrief."""
    print("=== Демо-режим DailyBrief ===")
    
    # Создаём несколько задач разных приоритетов
    todos = [
        {"task": "Прочитать книгу", "priority": "high"},
        {"task": "Сделать зарядку", "priority": "medium"},
        {"task": "Отправиться на прогулку", "priority": "low"},
    ]
    
    # Записываем их в файл (имитация сохранения)
    for todo in todos:
        with open("todos.txt", "a") as f:
            f.write(f"{todo['task']} [{todo['priority']}] {id(todo)}\n")
    print(f"Добавлено {len(todos)} задач в todos.txt")
    
    # Записываем заметки
    notes = [
        "Купить молоко",
        "Позвонить маме",
        "Записать идею для проекта",
    ]
    with open("notes.txt", "a") as f:
        for note in notes:
            f.write(f"{note}\n")
    print(f"Добавлено {len(notes)} заметок в notes.txt")
    
    # Записываем события
    events = [
        {"event": "Совещание", "time": "10:00"},
        {"event": "Обед с коллегами", "time": "13:00"},
    ]
    with open("events.txt", "a") as f:
        for ev in events:
            f.write(f"{ev['event']} {ev['time']}\n")
    print(f"Добавлено {len(events)} событий в events.txt")
    
    # Итоги дня
    summary = [
        {"result": "Успешно", "task": "Прочитать главу"},
        {"result": "Отменено", "task": "Зарядка (не хватило времени)"},
    ]
    with open("summary.txt", "a") as f:
        for s in summary:
            f.write(f"{s['result']}: {s['task']}\n")
    print(f"Добавлено {len(summary)} итогов в summary.txt")
    
    # Показываем содержимое файлов
    print("\n--- Результат ---")
    for fname in ["todos.txt", "notes.txt", "events.txt", "summary.txt"]:
        with open(fname) as f:
            content = f.read().strip()
            print(f"{fname}:\n{content}\n")

if __name__ == "__main__":
    demo_commands()
