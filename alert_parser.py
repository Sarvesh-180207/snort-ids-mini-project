
import json
from pathlib import Path
from datetime import datetime, timezone

BASE_DIR = Path(__file__).resolve().parent
LOG_DIR = BASE_DIR / "logs"
SAMPLE_FILE = LOG_DIR / "alerts.jsonl"


def parse_alerts():
    alerts = []

    if not LOG_DIR.exists():
        return alerts

    # Read the project's JSON Lines file and Snort JSON log files.
    files = [SAMPLE_FILE, LOG_DIR / "alert_json.txt"]

    for file_path in files:
        if not file_path.exists():
            continue

        try:
            with file_path.open("r", encoding="utf-8") as file:
                for line in file:
                    line = line.strip()
                    if not line:
                        continue

                    try:
                        record = json.loads(line)
                    except json.JSONDecodeError:
                        continue

                    timestamp = record.get("timestamp") or (
                        datetime.now(timezone.utc).isoformat()
                    )

                    alerts.append({
                        "timestamp": str(timestamp),
                        "message": str(
                            record.get("msg")
                            or record.get("message")
                            or record.get("rule")
                            or "Snort alert"
                        ),
                        "source": str(
                            record.get("src_ap")
                            or record.get("src_addr")
                            or record.get("source")
                            or "Unknown"
                        ),
                        "destination": str(
                            record.get("dst_ap")
                            or record.get("dst_addr")
                            or record.get("destination")
                            or "Unknown"
                        ),
                        "protocol": str(record.get("proto", "Unknown")),
                        "rule": str(record.get("rule", "Custom rule")),
                    })

        except OSError:
            continue

    # Most recent alerts first.
    alerts.reverse()
    return alerts
