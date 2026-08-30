# === Stage 36: Добавь проверку целостности данных и функцию ремонта простых проблем ===
# Project: DailyBrief
def verify_integrity(data):
    errors = []
    if not isinstance(data, dict):
        return errors
    required_keys = ['tasks', 'events', 'notes', 'priorities', 'day_summary']
    for key in required_keys:
        if key not in data:
            errors.append(f"Missing required key: {key}")
    if 'tasks' in data:
        for i, task in enumerate(data['tasks']):
            if not isinstance(task, dict) or 'title' not in task or 'priority' not in task:
                errors.append(f"Task {i} is malformed: {task}")
    if 'events' in data:
        for i, event in enumerate(data['events']):
            if not isinstance(event, dict) or 'date' not in event:
                errors.append(f"Event {i} is malformed: {event}")
    return errors

def repair_simple_issues(data):
    if not isinstance(data, dict):
        return {"error": "Input is not a dictionary", "original": data}
    repaired = data.copy()
    if 'tasks' not in repaired:
        repaired['tasks'] = []
    if 'events' not in repaired:
        repaired['events'] = []
    if 'notes' not in repaired:
        repaired['notes'] = []
    if 'priorities' not in repaired:
        repaired['priorities'] = {'critical': 0, 'high': 0, 'medium': 0, 'low': 0}
    if 'day_summary' not in repaired:
        repaired['day_summary'] = {'total_tasks': 0, 'completed': 0, 'pending': 0}
    return repaired
