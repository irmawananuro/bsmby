# === Stage 38: Добавь расширенный набор тестов для ошибок и пограничных случаев ===
# Project: DailyBrief
import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from daily_brief import DailyBrief

class TestEdgeCasesAndErrors(unittest.TestCase):

    def test_empty_input(self):
        db = DailyBrief()
        self.assertEqual(db.get_daily_brief(), "")

    def test_nonexistent_file(self):
        db = DailyBrief()
        with self.assertRaises(FileNotFoundError):
            db.load_file("nonexistent_file.txt")

    def test_invalid_json(self):
        db = DailyBrief()
        with self.assertRaises(ValueError):
            db.load_file("invalid.json")

    def test_large_input(self):
        db = DailyBrief()
        large_input = "\n".join(["task_" + "a" * 1000 for _ in range(100)])
        db.set_task(large_input)
        self.assertIn("task_", db.get_daily_brief())

    def test_special_characters(self):
        db = DailyBrief()
        special_input = "Task with special chars: @#$%^&*(){}[]|;:'\",<>?/~`"
        db.set_task(special_input)
        self.assertIn("@#$", db.get_daily_brief())

    def test_unicode_input(self):
        db = DailyBrief()
        unicode_input = "Задача с Unicode: 🚀🎉🐍"
        db.set_task(unicode_input)
        self.assertIn("🚀", db.get_daily_brief())

    def test_empty_task(self):
        db = DailyBrief()
        db.set_task("")
        self.assertEqual(db.get_daily_brief(), "")

    def test_duplicate_task(self):
        db = DailyBrief()
        db.set_task("Task 1")
        db.set_task("Task 1")
        brief = db.get_daily_brief()
        self.assertEqual(brief.count("Task 1"), 2)

    def test_mixed_case_task(self):
        db = DailyBrief()
        db.set_task("Task A")
        db.set_task("task a")
        brief = db.get_daily_brief()
        self.assertEqual(brief.count("Task A"), 2)

if __name__ == "__main__":
    unittest.main()
