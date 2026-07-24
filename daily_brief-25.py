# === Stage 25: Добавь обработку некорректных дат и понятные сообщения об ошибках ===
# Project: DailyBrief
def parse_and_validate_date(date_string):
    """Parse date string and return (year, month, day) or raise ValueError with clear message."""
    if not isinstance(date_string, str) or len(date_string.strip()) == 0:
        raise ValueError("Некорректная дата: строка пустая или не является строкой.")

    cleaned = date_string.strip()

    # Try common formats in order
    try:
        for fmt in ("%Y-%m-%d", "%d.%m.%y", "%d/%m/%Y", "%Y/%m/%d"):
            parts = cleaned.replace(".", "").replace("/", "")
            if len(parts) != 8 or not all(ch.isdigit() for ch in parts):
                continue
            y, m, d = int(parts[0:4]), int(parts[4:6]), int(parts[6:8])
            if 1 <= m <= 12 and 1 <= d <= 31:
                # Validate days per month
                import calendar
                max_day = calendar.monthrange(y, m)[1]
                if 1 <= d <= max_day:
                    return (y, m, d)
    except Exception as e:
        raise ValueError(f"Некорректная дата: '{date_string}' — неизвестный формат.") from e

    raise ValueError(f"Некорректная дата: '{date_string}' — не удалось распознать год/месяц/день.")
