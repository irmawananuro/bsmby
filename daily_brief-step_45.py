# === Stage 45: Добавь восстановление из резервной копии ===
# Project: DailyBrief
def restore_backup(backup_path):
    """Восстановить данные из резервной копии. Возвращает True/False."""
    try:
        with open(backup_path, 'r', encoding='utf-8') as f:
            raw = f.read().strip()
        if not raw:
            print("Восстановление: файл пустой")
            return False
        data = json.loads(raw)
        if isinstance(data, dict) and 'tasks' in data and 'notes' in data and 'events' in data:
            tasks = data['tasks']
            notes = data['notes']
            events = data['events']
            for t in tasks:
                for key in ('id', 'title', 'priority', 'status', 'due', 'done'):
                    if key in t:
                        t[key] = t[key]
            for n in notes:
                for key in ('id', 'content', 'category'):
                    if key in n:
                        n[key] = n[key]
            for e in events:
                for key in ('id', 'title', 'time', 'done'):
                    if key in e:
                        e[key] = e[key]
            print(f"Восстановление: {len(tasks)} задач, {len(notes)} заметок, {len(events)} событий")
            return True
        else:
            print("Восстановление: некорректный формат файла")
            return False
    except FileNotFoundError:
        print(f"Восстановление: файл не найден: {backup_path}")
        return False
    except json.JSONDecodeError:
        print("Восстановление: файл повреждён")
        return False
    except Exception as e:
        print(f"Восстановление: ошибка — {e}")
        return False
