# === Stage 9: Добавь импорт начальных данных из JSON-строки ===
# Project: DailyBrief
import json, os, datetime

def load_initial_data(json_string):
    try:
        data = json.loads(json_string)
        today = datetime.date.today().isoformat()
        if "daily_brief" not in data or data["daily_brief"].get("date") != today:
            brief = {
                "date": today,
                "tasks": [],
                "events": [],
                "notes": "",
                "priorities": {},
                "summary": ""
            }
            if not os.path.exists("data.json"):
                with open("data.json", "w", encoding="utf-8") as f:
                    json.dump(brief, f, ensure_ascii=False, indent=2)
        return data.get("daily_brief", brief)
    except (json.JSONDecodeError, KeyError):
        today = datetime.date.today().isoformat()
        return {
            "date": today,
            "tasks": [],
            "events": [],
            "notes": "",
            "priorities": {},
            "summary": ""
        }

INITIAL_DATA_JSON = '{"daily_brief":{"date":"2024-01-01","tasks":[],"events":[],"notes":"","priorities":{},"summary":""}}'
CURRENT_BRIEF = load_initial_data(INITIAL_DATA_JSON)
