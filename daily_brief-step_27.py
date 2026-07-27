# === Stage 27: Добавь функции сброса демо-данных и очистки состояния ===
# Project: DailyBrief
def reset_demo_data():
    """Сбрасывает все данные в демо-состояние."""
    global tasks, events, notes, priorities, day_summary, daily_stats
    tasks = [
        {"id": 1, "title": "Утренняя разминка", "priority": "high", "status": "done"},
        {"id": 2, "title": "Написать код DailyBrief", "priority": "high", "status": "in_progress"},
        {"id": 3, "title": "Позвонить родителям", "priority": "medium", "status": "pending"},
    ]
    events = [
        {"time": "08:00", "text": "Собрались на работу"},
        {"time": "12:30", "text": "Обед в столовой"},
        {"time": "17:00", "text": "Встреча с командой"},
    ]
    notes = [
        "Купить молоко и хлеб по дороге домой",
        "Записать идею для нового фича",
    ]
    priorities = {
        "high": 3,
        "medium": 5,
        "low": 2,
    }
    day_summary = "Продуктивный день: завершено 1 задача из 3, пропущено 0 встреч."
    daily_stats = {"total_tasks": 3, "completed": 1, "events_count": 3}

def clear_all_state():
    """Полностью очищает все данные и статистику."""
    global tasks, events, notes, priorities, day_summary, daily_stats
    tasks = []
    events = []
    notes = []
    priorities = {}
    day_summary = ""
    daily_stats = {"total_tasks": 0, "completed": 0, "events_count": 0}

reset_demo_data()
