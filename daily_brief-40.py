# === Stage 40: Добавь CLI-параметры через argparse для основных операций ===
# Project: DailyBrief
def main():
    import argparse
    parser = argparse.ArgumentParser(description="DailyBrief CLI")
    sub = parser.add_subparsers(dest="cmd", required=True)
    cmd_report = sub.add_parser("report", help="показать сводку дня")
    cmd_report.add_argument("--date", help="дата (YYYY-MM-DD)")
    cmd_task = sub.add_parser("task", help="добавить/показать задачу")
    cmd_task.add_argument("action", choices=["add", "list", "done"])
    cmd_task.add_argument("--title", help="название задачи")
    cmd_task.add_argument("--priority", choices=["low", "medium", "high"], default="medium")
    cmd_task.add_argument("--id", type=int, help="id задачи для завершения")
    cmd_event = sub.add_parser("event", help="добавить/показать событие")
    cmd_event.add_argument("action", choices=["add", "list"])
    cmd_event.add_argument("--title", help="название события")
    cmd_event.add_argument("--time", help="время (HH:MM)")
    cmd_note = sub.add_parser("note", help="добавить/показать заметку")
    cmd_note.add_argument("action", choices=["add", "list"])
    cmd_note.add_argument("--text", help="текст заметки")
    cmd_summary = sub.add_parser("summary", help="итоговый отчёт")
    args = parser.parse_args()

    if args.cmd == "report":
        print(f"DailyBrief — отчёт за {args.date}")
    elif args.cmd == "task":
        if args.action == "add":
            print(f"Задача добавлена: [{args.priority}] {args.title}")
        elif args.action == "list":
            print("Задачи:")
        elif args.action == "done":
            print(f"Задача {args.id} завершена")
    elif args.cmd == "event":
        if args.action == "add":
            print(f"Событие: {args.title} ({args.time})")
        elif args.action == "list":
            print("События:")
    elif args.cmd == "note":
        if args.action == "add":
            print(f"Заметка: {args.text}")
        elif args.action == "list":
            print("Заметки:")
    elif args.cmd == "summary":
        print("=== Итоги дня ===")

if __name__ == "__main__":
    main()
