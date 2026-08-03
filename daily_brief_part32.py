# === Stage 32: Добавь журнал действий пользователя ===
# Project: DailyBrief
class UserActionLogger:
    def __init__(self):
        self.entries = []

    def log(self, action_type, description, timestamp=None):
        if timestamp is None:
            import datetime
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = {"action": action_type, "description": description, "timestamp": timestamp}
        self.entries.append(entry)

    def get_summary(self):
        if not self.entries:
            return []
        today = datetime.datetime.now().date()
        today_entries = [e for e in self.entries if datetime.datetime.strptime(e["timestamp"], "%Y-%m-%d %H:%M:%S").date() == today]
        counts = {}
        for e in today_entries:
            counts[e["action"]] = counts.get(e["action"], 0) + 1
        return sorted(counts.items(), key=lambda x: -x[1])

    def get_all(self):
        return self.entries[-20:] if len(self.entries) > 20 else list(self.entries)


def print_user_actions_log(logger=None):
    if logger is None:
        logger = UserActionLogger()
    summary = logger.get_summary()
    all_entries = logger.get_all()
    print("\n=== Пользовательские действия ===")
    print(f"Сегодня: {summary}")
    print("Последние действия:")
    for entry in reversed(all_entries):
        print(f"  [{entry['timestamp']}] {entry['action']} - {entry['description']}")


def main():
    logger = UserActionLogger()
    logger.log("task_completed", "Завершил утреннюю задачу по Python-проект DailyBrief: Добавь журнал действий пользователя.")
    print_user_actions_log(logger)
