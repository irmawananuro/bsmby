# === Stage 7: Добавь сортировку записей по дате, приоритету и названию ===
# Project: DailyBrief
def sort_entries(entries, key='date'):
    if not entries: return []
    reverse = {'priority': True}.get(key, False)
    def _sort_key(e):
        val = e.get(key, '')
        try: return (0, int(val))
        except ValueError: return (1, str(val).lower())
    return sorted(entries, key=_sort_key, reverse=reverse)
