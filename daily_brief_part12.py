# === Stage 12: Добавь загрузку данных из локального JSON-файла с обработкой ошибок ===
# Project: DailyBrief
def load_daily_brief_from_json(filepath: str) -> dict | None:
    try:
        import json
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if not isinstance(data, dict):
            raise ValueError("JSON root must be an object")
        required_keys = ['tasks', 'events', 'notes', 'priorities', 'summary']
        missing = [k for k in required_keys if k not in data]
        if missing:
            raise KeyError(f"Missing keys: {missing}")
        return data
    except FileNotFoundError:
        print(f"[WARN] File '{filepath}' not found. Using empty brief.")
        return {}
    except json.JSONDecodeError as e:
        print(f"[ERROR] Invalid JSON in '{filepath}': {e}")
        return None
    except Exception as e:
        print(f"[ERROR] Unexpected error loading '{filepath}': {type(e).__name__}: {e}")
        return None
