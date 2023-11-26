# /tests/test_anomaly_detection.py
import unittest
from app.core.anomaly_detection import detect_anomalies

class TestAnomalyDetection(unittest.TestCase):
    def test_detect_anomalies(self):
        # Placeholder test for anomaly detection
        correlated_data = [{"log_entry": "error 123", "type": "error"}, {"log_entry": "info 456", "type": "info"}]
        anomalies = detect_anomalies(correlated_data)
        self.assertIsNotNone(anomalies)
        self.assertGreaterEqual(len(anomalies), 0)

if __name__ == '__main__':
    unittest.main()

