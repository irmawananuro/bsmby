# === Stage 34: Добавь простую систему шаблонов для быстрого создания записей ===
# Project: DailyBrief
TEMPLATE_REGISTRY = {}

def register_template(name, default_text):
    """Регистрирует шаблон по имени."""
    TEMPLATE_REGISTRY[name] = default_text

def create_from_template(template_name, **kwargs):
    """Создаёт запись из шаблона, заполняя ключевые поля."""
    text = TEMPLATE_REGISTRY.get(template_name, "Текст шаблона не найден.")
    if kwargs:
        for key, value in kwargs.items():
            text = text.replace("{{" + key + "}}", str(value))
    return text.strip()

register_template("daily_task", "Задача: {{title}}\nПриоритет: {{priority}}\nСтатус: {{status}}\nПримечание: {{note}}")
register_template("daily_event", "Событие: {{event_name}}\nВремя: {{time}}\nМесто: {{place}}")
register_template("daily_note", "Заметка: {{title}}\nДетали: {{content}}\nТеги: {{tags}}")
register_template("daily_priority", "Приоритет: {{level}}\nЗадачи: {{tasks}}\nКомментарий: {{comment}}")
register_template("daily_summary", "Итоги дня:\n{{date}}\nЗавершено: {{completed}}\nПромедлено: {{pending}}\nНастроение: {{mood}}")
