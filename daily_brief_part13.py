# === Stage 13: Добавь поиск по нескольким полям без учёта регистра ===
# Project: DailyBrief
def multi_field_search(query, data_list, fields=None):
    if not query or not data_list:
        return []
    if fields is None:
        fields = ['task', 'event', 'note', 'priority', 'summary']
    query_lower = query.lower().strip()
    results = [item for item in data_list if any(query_lower in str(getattr(item, field, '')).lower() for field in fields)]
    return results
