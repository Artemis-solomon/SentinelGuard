# SentinelGuard API Reference

SentinelGuard provides a set of APIs for integration and customization. The APIs cover various functionalities related to log analysis, anomaly detection, and more.

## Table of Contents

1. [Log Parser API](#log-parser-api)
2. [Log Correlation API](#log-correlation-api)
3. [Anomaly Detection API](#anomaly-detection-api)
4. [Alerting API](#alerting-api)
5. [Dashboard API](#dashboard-api)
6. [Search and Query API](#search-and-query-api)

## Log Parser API

### `parse_log(log_file_path: str) -> List[str]`

Parses log entries from the specified log file.

- **Parameters:**
  - `log_file_path` (str): Path to the log file.

- **Returns:**
  - `List[str]`: List of parsed log entries.

## Log Correlation API

### `correlate_logs(log_entries: List[str]) -> List[Dict[str, Union[str, int]]]`

Correlates log entries to identify patterns and relationships.

- **Parameters:**
  - `log_entries` (List[str]): List of log entries.

- **Returns:**
  - `List[Dict[str, Union[str, int]]]`: List of correlated log entries with additional information.

## Anomaly Detection API

### `detect_anomalies(correlated_logs: List[Dict[str, Union[str, int]]]) -> List[Dict[str, Union[str, int]]]`

Detects anomalies in correlated log entries using machine learning algorithms.

- **Parameters:**
  - `correlated_logs` (List[Dict[str, Union[str, int]]]): List of correlated log entries.

- **Returns:**
  - `List[Dict[str, Union[str, int]]]`: List of detected anomalies with additional information.

## Alerting API

### `send_alert(alert_message: str) -> None`

Sends a real-time alert for a detected security incident.

- **Parameters:**
  - `alert_message` (str): Message describing the security incident.

- **Returns:**
  - `None`

## Dashboard API

### `get_dashboard_data() -> Dict[str, Any]`

Retrieves data for the user-friendly dashboard.

- **Returns:**
  - `Dict[str, Any]`: Dashboard data including log entry overview, correlation information, and real-time alerts.

## Search and Query API

### `search_logs(query: str) -> List[str]`

Searches log entries based on the specified query.

- **Parameters:**
  - `query` (str): Search query.

- **Returns:**
  - `List[str]`: List of log entries matching the query.

For more details on API usage, refer to the corresponding functions in the source code.

Feel free to integrate these APIs into your workflows or applications for seamless log analysis and anomaly detection.

