# /tests/test_log_parser.py
import unittest
from app.core.log_parser import parse_log

class TestLogParser(unittest.TestCase):
    def test_parse_log(self):
        # Placeholder test for log parsing
        log_file_path = "sample.log"
        log_entries = parse_log(log_file_path)
        self.assertIsNotNone(log_entries)
        self.assertGreater(len(log_entries), 0)

if __name__ == '__main__':
    unittest.main()

