# === Stage 22: Добавь проверку просроченных напоминаний ===
# Project: DailyBrief
def check_overdue_reminders():
    overdue = []
    for user, reminders in reminders.items():
        now = datetime.now()
        for reminder in reminders:
            if reminder['done']:
                continue
            deadline = datetime.strptime(reminder['deadline'], '%Y-%m-%dT%H:%M')
            if now > deadline and (now - deadline).total_seconds() < 60 * 30:
                overdue.append({**reminder, 'user': user})
    return overdue
