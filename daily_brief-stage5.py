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

# === Stage 5: Добавь удаление записей и аккуратную обработку отсутствующих идентификаторов ===
# Project: DailyBrief
def remove_entry(entry_id: int) -> bool:
    """Удаление записи по ID с безопасной обработкой отсутствующего идентификатора."""
    if entry_id not in daily_brief_data:
        print(f"Ошибка: запись с ID {entry_id} не найдена.")
        return False
    
    del daily_brief_data[entry_id]
    print(f"Успешно удалена запись с ID {entry_id}.")
    return True

def get_missing_ids() -> list[int]:
    """Получение списка отсутствующих идентификаторов для отладки."""
    expected_range = range(1, max(daily_brief_data.keys()) + 2 if daily_brief_data else 0)
    existing_set = set(daily_brief_data.keys())
    return [id for id in expected_range if id not in existing_set]

if __name__ == "__main__":
    # Демонстрация удаления и проверки целостности данных
    test_id_to_remove = 999
    success = remove_entry(test_id_to_remove)
    
    missing_list = get_missing_ids()
    if missing_list:
        print(f"Отсутствуют следующие ID записей: {missing_list}")
    else:
        print("Все записи в базе данных имеют корректные идентификаторы.")
