# === Stage 20: Добавь восстановление записей из архива ===
# Project: DailyBrief
def restore_from_archive():
    """Восстанавливает записи из текстового архива в словарь."""
    archive_path = input("Путь к файлу-архиву: ").strip() or "archive.txt"
    if not os.path.exists(archive_path):
        print(f"Файл {archive_path} не найден.")
        return {}

    records = {}
    with open(archive_path, 'r', encoding='utf-8') as f:
        raw_lines = [l.strip() for l in f if l.strip()]

    current_key = None
    for line in raw_lines:
        parts = line.split('=', 1)
        if len(parts) == 2 and not parts[0].strip():
            current_key = parts[1].strip()
            records[current_key] = []
        elif current_key is not None:
            value = parts[1].strip().replace('\n', ' ')
            records[current_key].append(value)

    return records
