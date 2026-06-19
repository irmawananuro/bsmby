# === Stage 4: Добавь функцию редактирования существующих записей по идентификатору ===
# Project: DailyBrief
def edit_record(record_id, updates):
    records = get_all_records()
    if record_id not in records:
        print(f"Ошибка: запись с ID {record_id} не найдена.")
        return False
    
    index = next((i for i, r in enumerate(records) if r['id'] == record_id), None)
    if index is None:
        return False

    current_record = records[index]
    
    # Обновляем только предоставленные поля
    for key, value in updates.items():
        if key in current_record:
            current_record[key] = value
    
    # Сохраняем изменения (предполагается глобальная функция save_records или запись в файл)
    # Если данные хранятся в памяти, нужно пересоздать список records с обновленными данными
    updated_records = [r for i, r in enumerate(records)]
    if index is not None:
        updated_records[index] = current_record
    
    # Здесь должна быть логика сохранения (например, запись в JSON файл)
    # Для примера предположим, что есть функция save_to_file или аналогичная
    try:
        with open('daily_brief_data.json', 'w') as f:
            import json
            json.dump(updated_records, f, indent=4)
        print(f"Запись с ID {record_id} успешно обновлена.")
        return True
    except Exception as e:
        print(f"Ошибка при сохранении изменений: {e}")
        return False
