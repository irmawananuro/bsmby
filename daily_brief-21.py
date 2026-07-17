# === Stage 21: Добавь простую систему напоминаний с датой выполнения ===
# Project: DailyBrief
import datetime


class Reminder:
    def __init__(self, text, date, time=None):
        self.text = text
        self.date = datetime.date.fromisoformat(date)
        self.time = datetime.time.fromisoformat(time) if time else None
        self.done = False

    @property
    def is_due(self):
        now = datetime.datetime.now()
        return (self.date <= now.date()) and not self.done

    def __repr__(self):
        status = "✓" if self.done else "○"
        due_str = f"{self.time} " if self.time else ""
        return f"[{status}] {due_str}{self.text}"


def add_reminders(reminders, text="", date=None, time=None):
    reminder = Reminder(text, date, time)
    reminders.append(reminder)
    return reminder


def get_due_reminders(reminders):
    return [r for r in reminders if r.is_due]


# Пример использования:
if __name__ == "__main__":
    my_reminders = []
    add_reminders(my_reminders, "Выпить воду", "2025-12-31")
    add_reminders(my_reminders, "Учесть встречу", "2026-01-15", time="14:00")
    print("Срочные напоминания:", get_due_reminders(my_reminders))
