# === Stage 1: Создай базовую структуру файла приложения, точку входа и демонстрационные данные ===
# Project: DailyBrief
import json, os, datetime as dt
from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class Task:
    id: int
    title: str
    priority: int  # 1-5
    status: str = "pending"
    notes: str = ""

def load_sample_data() -> dict[str, any]:
    tasks = [Task(1, "Сделать утреннюю пробежку", 3), Task(2, "Прочитать главу книги", 4)]
    events = [{"id": 101, "title": "Встреча с командой", "time": dt.datetime.now().strftime("%H:%M"), "location": "Конференц-зал"}]
    notes = ["Купить молоко", "Позвонить маме"]
    summary = {"mood": "Хорошо", "highlights": "Завершил проект по автоматизации"}
    
    data_dir = os.path.join(os.path.dirname(__file__), "data")
    os.makedirs(data_dir, exist_ok=True)
    
    with open(os.path.join(data_dir, "sample.json"), "w", encoding="utf-8") as f:
        json.dump({"tasks": [t.__dict__ for t in tasks], "events": events, "notes": notes, "summary": summary}, f, ensure_ascii=False)
    
    return {"tasks": tasks, "events": events, "notes": notes, "summary": summary}

if __name__ == "__main__":
    data = load_sample_data()
    print(f"Загружено {len(data['tasks'])} задач и {len(data['events'])} событий.")
