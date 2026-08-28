# === Stage 35: Добавь рекомендации следующего действия на основе текущего состояния ===
# Project: DailyBrief
def next_action():
    if not todos:
        return "Nothing to do. Take a break or start a new task."
    priority_order = {"critical": 0, "high": 1, "medium": 2, "low": 3}
    sorted_todos = sorted(todos, key=lambda t: priority_order.get(t.get("priority", "low"), 3))
    return sorted_todos[0]["name"] + " (priority: " + sorted_todos[0]["priority"] + ")"
