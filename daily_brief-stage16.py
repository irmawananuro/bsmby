# === Stage 16: Добавь расчёт месячной статистики по датам ===
# Project: DailyBrief
def monthly_stats(daily_data):
    """Calculate monthly statistics from daily data."""
    stats = {}
    for date, day in sorted(daily_data.items()):
        month_key = f"{date.year}-{date.month:02d}"
        if month_key not in stats:
            stats[month_key] = {
                "days": 0,
                "tasks_completed": 0,
                "events_count": 0,
                "notes_count": 0,
                "priorities": {},
                "summaries": 0,
            }
        stats[month_key]["days"] += 1
        if day.get("completed", False):
            stats[month_key]["tasks_completed"] += 1
        stats[month_key]["events_count"] = len(day.get("events", []))
        stats[month_key]["notes_count"] = len(day.get("notes", []))
        for p in day.get("priorities", {}):
            stats[month_key]["priorities"][p] = stats[month_key].get("priorities", {}).get(p, 0) + 1
        if day.get("summary"):
            stats[month_key]["summaries"] += 1
    return stats
