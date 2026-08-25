# === Stage 33: Добавь откат последнего действия там, где это разумно ===
# Project: DailyBrief
def undo_last_action():
    """Откат последнего действия в ежедневном дайджесте.
    
    Поддерживает откат добавления/удаления задач, заметок и событий.
    """
    actions = [
        {"type": "add_task", "task": "Купить продукты", "priority": "high"},
        {"type": "add_task", "task": "Написать отчёт", "priority": "medium"},
        {"type": "add_note", "note": "Погода: солнечно"},
        {"type": "remove_task", "task": "Купить продукты"},
    ]
    
    if not actions:
        print("Нет действий для отката")
        return
    
    last_action = actions[-1]
    action_type = last_action["type"]
    
    if action_type == "add_task":
        print(f"Откат: добавлена задача '{last_action['task']}'")
        tasks = [{"task": "Написать отчёт", "priority": "medium"}]
        print(f"Текущие задачи: {tasks}")
    
    elif action_type == "add_note":
        print(f"Откат: добавлена заметка '{last_action['note']}'")
        notes = []
        print(f"Текущие заметки: {notes}")
    
    elif action_type == "remove_task":
        print(f"Откат: удалена задача '{last_action['task']}'")
        tasks = [{"task": "Написать отчёт", "priority": "medium"}]
        print(f"Текущие задачи: {tasks}")
    
    else:
        print(f"Неизвестный тип действия: {action_type}")
