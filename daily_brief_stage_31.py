# === Stage 31: Добавь переключение активного пользовательского профиля ===
# Project: DailyBrief
def switch_profile(current, new):
    if new not in profiles:
        print(f"Ошибка: профиль '{new}' не найден.")
        return False
    current["active"] = new
    print(f"Активный профиль изменён на: {new}")
    return True

def list_profiles():
    for name, info in profiles.items():
        status = "✓ активен" if info.get("active") else ""
        print(f"{name}: {status}")
