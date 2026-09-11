# === Stage 44: Добавь функцию резервного копирования файла данных ===
# Project: DailyBrief
import shutil
from datetime import datetime, timezone

def backup_data_file(source_path, backup_dir=None):
    if backup_dir is None:
        backup_dir = "backups"
    os.makedirs(backup_dir, exist_ok=True)
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(backup_dir, f"{os.path.basename(source_path)}.{timestamp}")
    shutil.copy2(source_path, backup_path)
    return backup_path
