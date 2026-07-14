# === Stage 19: Добавь функцию архивации завершённых или старых записей ===
# Project: DailyBrief
import datetime

def archive_old_entries(entries, cutoff_days=30):
    """Archive entries older than cutoff_days and return list of archived items."""
    now = datetime.datetime.now()
    cutoff = now - datetime.timedelta(days=cutoff_days)
    archived = []
    active = []
    for entry in entries:
        date_str = entry.get('date', '')
        try:
            entry_date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
            if entry_date < cutoff.date():
                archived.append(entry)
            else:
                active.append(entry)
        except ValueError:
            active.append(entry)
    return active, archived
