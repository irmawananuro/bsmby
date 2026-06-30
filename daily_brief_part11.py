# === Stage 11: Добавь сохранение данных в локальный JSON-файл ===
# Project: DailyBrief
import json, os
DATA_FILE = "dailybrief_data.json"

def save_state(data):
    try:
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except IOError as e:
        print(f"[Ошибка сохранения] {e}")

def load_state():
    if not os.path.exists(DATA_FILE):
        return {"tasks": [], "events": [], "notes": [], "priorities": {}, "summary": ""}
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (IOError, json.JSONDecodeError):
        print("[Ошибка загрузки] Файл повреждён или отсутствует. Создаётся новый.")
        return {"tasks": [], "events": [], "notes": [], "priorities": {}, "summary": ""}

def get_state():
    state = load_state()
    # Обновляем текущие данные в памяти перед сохранением, если это не первый запуск
    if not os.path.exists(DATA_FILE):
        save_state(state)
    return state
