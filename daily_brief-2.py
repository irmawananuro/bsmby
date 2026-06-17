# === Stage 2: Добавь модели данных и функции валидации пользовательского ввода ===
# Project: DailyBrief
class DailyBriefModel:
    def __init__(self):
        self.tasks = []
        self.events = []
        self.notes = []
        self.results = {}

    def validate_task(self, title: str, priority: int) -> bool:
        if not title.strip(): return False
        if not 1 <= priority <= 5: return False
        return True

    def add_task(self, task_data):
        if not isinstance(task_data, dict): return False
        if 'title' not in task_data or 'priority' not in task_data: return False
        if self.validate_task(task_data['title'], task_data['priority']):
            self.tasks.append({'id': len(self.tasks) + 1, **task_data})
            return True
        return False

    def validate_event(self, title: str, date_str: str) -> bool:
        if not title.strip(): return False
        try: from datetime import datetime; datetime.strptime(date_str, '%Y-%m-%d')
        except ValueError: return False
        return True

    def add_event(self, event_data):
        if not isinstance(event_data, dict): return False
        if 'title' not in event_data or 'date' not in event_data: return False
        if self.validate_event(event_data['title'], event_data['date']):
            self.events.append({'id': len(self.events) + 1, **event_data})
            return True
        return False

    def add_note(self, note_text: str):
        if not isinstance(note_text, str): return False
        if not note_text.strip(): return False
        self.notes.append({'id': len(self.notes) + 1, 'text': note_text})
        return True

    def record_result(self, category: str, value: float):
        if not isinstance(category, str) or not isinstance(value, (int, float)): return False
        if category in self.results: self.results[category] += value
        else: self.results[category] = value
