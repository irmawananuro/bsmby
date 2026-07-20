# === Stage 23: Добавь форматированный вывод таблицей в консоль ===
# Project: DailyBrief
def print_daily_brief(tasks, events, notes, priorities, summary):
    """Выводит ежедневный дайджест в формате таблицы в консоль."""
    width = 40
    sep = "=" * width
    print(sep)
    print(f"📅 DailyBrief — {datetime.now().strftime('%d.%m.%Y %H:%M')}\n")
    
    if tasks:
        print(f"{'Задачи':>{width}} | {'Приоритет':>10}")
        for t in tasks:
            priority = priorities.get(t, 'Низкий')
            print(f"{t:{width}} | {priority:>10}")
    
    if events:
        print(sep)
        print(f"{'События':>{width}}")
        for e in events:
            print(f"{e:{width}}")
    
    if notes:
        print(sep)
        print("Заметки:")
        for n in notes:
            print(f"  • {n}")
    
    if summary:
        print(sep)
        print(summary[:width])

print_daily_brief(tasks, events, notes, priorities, summary)
