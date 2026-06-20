# === Stage 5: Добавь удаление записей и аккуратную обработку отсутствующих идентификаторов ===
# Project: DailyBrief
def delete_entry(entry_id: int) -> bool:
    """Удалить запись по ID, вернуть True если удалено."""
    if entry_id not in _entries:
        print(f"Ошибка: запись с id={entry_id} не найдена.")
        return False
    
    del _entries[entry_id]
    print(f"Запись с id={entry_id} успешно удалена.")
    return True

def handle_missing_ids(entries_data, target_key="id"):
    """Проверить и обработать отсутствующие идентификаторы в данных."""
    valid_entries = []
    missing_ids = set()
    
    for item in entries_data:
        if target_key not in item or not isinstance(item[target_key], int):
            print(f"Предупреждение: запись без корректного {target_key} пропущена.")
            continue
        
        valid_entries.append(item)
        
    return valid_entries, missing_ids

def sanitize_and_store(entries_data, storage_dict):
    """Очистить данные от отсутствующих ID и сохранить в хранилище."""
    cleaned_data = handle_missing_ids(entries_data)
    
    for item in cleaned_data:
        entry_id = item.get("id")
        
        if entry_id is not None and isinstance(entry_id, int):
            storage_dict[entry_id] = item
            
    return len(storage_dict), sum(1 for _ in entries_data if "id" in _)
