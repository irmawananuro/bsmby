# === Stage 41: Добавь режим dry-run для операций изменения данных ===
# Project: DailyBrief
def dry_run(operation, params=None):
    """Simulate an operation without changing state. Returns a dict with the
    original data and a simulated result."""
    if params is None:
        params = {}
    result = {"status": "dry-run", "original": params}
    if operation == "add_task":
        result["simulated"] = {"id": len(tasks) + 1, "text": params.get("text", ""), "priority": params.get("priority", "medium")}
    elif operation == "add_event":
        result["simulated"] = {"id": len(events) + 1, "text": params.get("text", ""), "date": params.get("date", ""), "importance": params.get("importance", "normal")}
    elif operation == "add_note":
        result["simulated"] = {"id": len(notes) + 1, "text": params.get("text", ""), "date": params.get("date", "")}
    elif operation == "set_priority":
        result["simulated"] = {"task_id": params.get("task_id"), "new_priority": params.get("priority", "medium")}
    elif operation == "add_summary":
        result["simulated"] = {"date": params.get("date", ""), "summary": params.get("summary", "")}
    elif operation == "set_goal":
        result["simulated"] = {"date": params.get("date", ""), "goal": params.get("goal", "")}
    else:
        result["error"] = f"Unknown operation: {operation}"
    return result
