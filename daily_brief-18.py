# === Stage 18: Добавь поддержку тегов и операции добавления/удаления тегов ===
# Project: DailyBrief
def add_tag(entry_id, tag):
    entry = find_entry_by_id(entry_id)
    if not entry:
        return False
    if tag in entry["tags"]:
        print(f"Tag '{tag}' already exists for this entry.")
        return True
    entry.setdefault("tags", []).append(tag)
    save()
    print(f"Added tag '{tag}'.")
    return True

def remove_tag(entry_id, tag):
    entry = find_entry_by_id(entry_id)
    if not entry:
        return False
    tags = entry.get("tags", [])
    if tag in tags:
        tags.remove(tag)
        save()
        print(f"Removed tag '{tag}'.")
        return True
    else:
        print(f"Tag '{tag}' is not present.")
        return False

def list_tags(entry_id):
    entry = find_entry_by_id(entry_id)
    if not entry:
        print("No such entry.")
        return
    tags = entry.get("tags", [])
    if not tags:
        print("This entry has no tags yet.")
        return
    print(f"Tags for this entry: {', '.join(tags)}")

def delete_entry_by_id(entry_id):
    entries = load()
    result = [e for e in entries if e["id"] != entry_id]
    if len(result) == 0:
        print("No such entry.")
        return False
    save(result)
    print(f"Deleted entry with id '{entry_id}'.")
    return True

def get_daily_summary():
    entries = load()
    today = datetime.date.today().isoformat()
    daily = [e for e in entries if e.get("date") == today]
    if not daily:
        print("No entries for this day yet.")
        return None
    tasks = [e for e in daily if "task" in e.get("type", "")]
    events = [e for e in daily if "event" in e.get("type", "")]
    notes = [e for e in daily if "note" in e.get("type", "")]
    priorities = [e for e in daily if "priority" in e.get("type", "")]
    
    print(f"\n--- Daily Brief ---")
    print(f"Date: {today}")
    print(f"Total entries: {len(daily)}")
    print(f"Tasks: {len(tasks)}")
    print(f"Events: {len(events)}")
    print(f"Notes: {len(notes)}")
    
    if priorities:
        total_priority = sum(int(e.get("value", 0)) for e in priorities)
        avg_priority = f"{total_priority / len(priorities):.1f}"
        print(f"Priority (avg): {avg_priority}")
