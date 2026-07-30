# === Stage 29: Добавь конфигурацию приложения через словарь настроек ===
# Project: DailyBrief
APP_CONFIG = {
    "app_name": "DailyBrief",
    "version": "1.0.29",
    "language": "ru",
    "timezone": None,  # auto-detect if None
    "display_format": "compact",  # compact | detailed
    "date_prefix": True,
    "sections_order": [
        "tasks",
        "events",
        "notes",
        "priorities",
        "day_summary",
    ],
    "task_priority_levels": ["low", "medium", "high"],
    "max_notes_display": 10,
    "theme_colors": {
        "bg": "#1e1e2e",
        "fg": "#cdd6f4",
        "accent": "#89b4fa",
        "task_done": "#a6e3a1",
        "task_pending": "#f38ba8",
    },
}


def get_config():
    return APP_CONFIG.copy()
