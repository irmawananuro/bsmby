# === Stage 6: Добавь фильтрацию записей по статусу, категории или тегам ===
# Project: DailyBrief
def filter_records(records, filters=None):
    if not filters: return records
    result = []
    for r in records:
        match_status = (filters.get('status') is None) or (r.get('status') == filters['status'])
        match_category = (filters.get('category') is None) or (r.get('category') == filters['category'])
        match_tags = (filters.get('tags') is None) or any(t in r.get('tags', []) for t in filters['tags'])
        if match_status and match_category and match_tags: result.append(r)
    return result

# Пример вызова с фильтрацией по статусу "done" и категории "work":
# filtered = filter_records(all_records, {'status': 'done', 'category': 'work'})
