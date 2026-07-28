# === Stage 28: Добавь подсчёт ключевых метрик проекта ===
# Project: DailyBrief
def project_metrics(tasks, events, notes, priorities):
    total_tasks = len(tasks)
    completed = sum(1 for t in tasks if t['status'] == 'done')
    overdue = sum(1 for t in tasks if t.get('due') and datetime.now() > datetime.strptime(t['due'], '%Y-%m-%d'))

    high_priority_events = sum(1 for e in events if e.get('priority') == 'high')
    event_types = set(e.get('type', 'unknown') for e in events)

    notes_by_topic = {}
    for n in notes:
        topic = n.get('topic', 'general').lower()
        notes_by_topic[topic] = notes_by_topic.get(topic, 0) + 1

    priority_dist = {}
    for p in priorities:
        key = p.get('level', 'unknown')
        priority_dist[key] = priority_dist.get(key, 0) + 1

    metrics = {
        'total_tasks': total_tasks,
        'completed': completed,
        'completion_rate': (completed / total_tasks * 100) if total_tasks else 0,
        'overdue_tasks': overdue,
        'high_priority_events': high_priority_events,
        'event_types_count': len(event_types),
        'notes_by_topic': notes_by_topic,
        'priority_distribution': priority_dist,
    }
    return metrics
