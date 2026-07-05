# === Stage 14: Добавь генерацию краткой сводки по текущим данным ===
# Project: DailyBrief
def generate_daily_brief(tasks, events, notes, priorities, summaries):
    """Генерирует текстовую сводку дня на основе текущих данных."""
    lines = ["=== ДАЙДЖЕСТ ЗАВТРАШНЕГО ДНЯ ===", ""]
    
    if tasks:
        high_priority = [t for t in tasks if t.get('priority') == 'high']
        lines.append(f"📌 Задачи (высокий приоритет): {len(high_priority)}")
        for task in high_priority[:3]:  # Ограничиваем вывод топ-3
            lines.append(f"   - [{task['status']}] {task.get('title', 'Без названия')}")
    
    if events:
        today_events = [e for e in events if e.get('date') == 'today' or not e.get('date')]
        if today_events:
            lines.append(f"📅 События сегодня ({len(today_events)}):")
            for event in today_events[:3]:
                lines.append(f"   - {event.get('title', 'Без названия')} в {event.get('time', 'не указано')}")
    
    if notes:
        urgent_notes = [n for n in notes if n.get('tag') == 'urgent']
        if urgent_notes:
            lines.append(f"⚠️ Срочные заметки ({len(urgent_notes)}):")
            for note in urgent_notes[:2]:
                lines.append(f"   - {note.get('content', '')}")
    
    if priorities:
        top_priorities = sorted(priorities, key=lambda x: x['score'], reverse=True)[:3]
        if top_priorities:
            lines.append(f"🏆 Топ-приоритеты дня:")
            for p in top_priorities:
                lines.append(f"   - {p.get('name', 'Приоритет')} ({p.get('score', 0)} баллов)")
    
    if summaries:
        daily_summary = summaries.get('today') or summaries.get('default')
        if daily_summary:
            lines.append(f"\n💡 Итог дня:\n{daily_summary}")
    
    return "\n".join(lines)
