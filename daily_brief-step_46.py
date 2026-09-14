# === Stage 46: Добавь миграцию версии структуры данных ===
# Project: DailyBrief
def migrate_version_structure(version, data):
    """
    Миграция структуры данных: добавление полей для новых версий.

    Args:
        version (int): Текущая версия структуры данных.
        data (dict): Текущий словарь данных.

    Returns:
        dict: Обновлённый словарь данных с новыми полями.
    """
    if version < 2:
        data.setdefault('tasks', [])
        data.setdefault('events', [])
        data.setdefault('notes', [])
        data.setdefault('priorities', {})
        data.setdefault('daily_summary', {})
        data['version'] = version
    elif version < 3:
        data.setdefault('tasks', [])
        data.setdefault('events', [])
        data.setdefault('notes', [])
        data.setdefault('priorities', {})
        data.setdefault('daily_summary', {})
        data['version'] = version
    elif version < 4:
        data.setdefault('tasks', [])
        data.setdefault('events', [])
        data.setdefault('notes', [])
        data.setdefault('priorities', {})
        data.setdefault('daily_summary', {})
        data['version'] = version
    else:
        data['version'] = version
    return data
