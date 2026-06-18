# === Stage 3: Реализуй хранение состояния в памяти и функции добавления записей ===
# Project: DailyBrief
class DailyBrief:
    def __init__(self):
        self._state = {
            "tasks": [],
            "events": [],
            "notes": [],
            "priorities": {},
            "summary": {}
        }

    def add_task(self, title: str, priority: int = 1) -> None:
        task_id = len(self._state["tasks"]) + 1
        self._state["tasks"].append({"id": task_id, "title": title, "priority": priority})

    def add_event(self, event_name: str, date: str) -> None:
        event_id = len(self._state["events"]) + 1
        self._state["events"].append({"id": event_id, "name": event_name, "date": date})

    def add_note(self, content: str) -> None:
        note_id = len(self._state["notes"]) + 1
        self._state["notes"].append({"id": note_id, "content": content})

    def set_priority(self, task_id: int, new_priority: int) -> bool:
        for task in self._state["tasks"]:
            if task["id"] == task_id:
                task["priority"] = new_priority
                return True
        return False

    def add_summary_item(self, key: str, value: str) -> None:
        self._state["summary"][key] = value
