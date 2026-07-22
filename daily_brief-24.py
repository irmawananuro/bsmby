# === Stage 24: Добавь компактный вывод одной записи с деталями ===
# Project: DailyBrief
def show_entry(entry):
    """Компактный вывод одной записи с деталями."""
    print(f"[{entry.get('timestamp', '???')}] {entry['title']}")
    for k, v in entry.items():
        if k not in ('title', 'timestamp'):
            print(f"  {k}: {v}")

# Пример:
show_entry({
    "title": "Купить хлеб",
    "status": "done",
    "priority": "low",
    "note": "Был в магазине с 10 до 12",
})
