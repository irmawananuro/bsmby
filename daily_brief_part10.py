# === Stage 10: Добавь экспорт текущего состояния в JSON-строку ===
# Project: DailyBrief
def export_to_json():
    from datetime import datetime
    data = {
        "timestamp": datetime.utcnow().isoformat(),
        "tasks": tasks,
        "events": events,
        "notes": notes,
        "priorities": priorities,
        "summary": summary
    }
    return json.dumps(data, ensure_ascii=False, indent=2)
