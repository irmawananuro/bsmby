# === Stage 15: Добавь расчёт недельной статистики по датам ===
# Project: DailyBrief
def weekly_stats(daily_data):
    weeks = {}
    for date, entry in daily_data.items():
        week_start = (date - datetime.timedelta(days=date.weekday())).strftime('%Y-%m-%d')
        if week_start not in weeks:
            weeks[week_start] = {'tasks': 0, 'events': 0, 'notes': 0, 'priority_high': 0, 'priority_medium': 0, 'priority_low': 0}
        weeks[week_start]['tasks'] += entry.get('tasks', [])
        weeks[week_start]['events'] += entry.get('events', [])
        weeks[week_start]['notes'] += entry.get('notes', [])
        for task in entry.get('tasks', []):
            if task['priority'] == 1:
                weeks[week_start]['priority_high'] += 1
            elif task['priority'] == 2:
                weeks[week_start]['priority_medium'] += 1
            else:
                weeks[week_start]['priority_low'] += 1
    return weeks
