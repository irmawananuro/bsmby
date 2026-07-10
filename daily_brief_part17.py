# === Stage 17: Добавь группировку записей по категориям ===
# Project: DailyBrief
def group_entries_by_category(entries):
    grouped = {}
    for entry in entries:
        cat = entry.get("category", "Uncategorized")
        if cat not in grouped:
            grouped[cat] = []
        grouped[cat].append(entry)
    return grouped
