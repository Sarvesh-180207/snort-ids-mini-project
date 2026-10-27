
# Intrusion Detection System Using Snort

## Project Overview
This Network Security mini project demonstrates how Snort detects
selected network traffic patterns using custom IDS rules. A local
Flask dashboard displays recorded alert events.

## Objectives
- Understand signature-based intrusion detection.
- Create and inspect custom Snort rules.
- Observe security alerts from authorized lab traffic.
- Parse JSON alert records with Python.
- Display events in a browser dashboard.
- Maintain project source code with Git.

## Technologies
- Snort IDS
- Ubuntu Linux / WSL
- Python
- Flask
- HTML and CSS
- JSON Lines
- Git and GitHub

## Project Files
- app.py: Flask dashboard backend
- alert_parser.py: Reads Snort JSON alert records
- rules/local.rules: Custom detection rules
- logs/alerts.jsonl: Sample alert records
- templates/index.html: Dashboard layout
- static/style.css: Dashboard styling
- reports/output.txt: Demonstration output
- requirements.txt: Python dependencies

## Run the Dashboard on Windows
1. Install Python and Git.
2. Create a virtual environment.
3. Install requirements.
4. Run python app.py.
5. Open http://127.0.0.1:5000.

## Snort Setup
Install a compatible Snort version in Ubuntu or another supported
Linux environment. Verify the version and available command options.
Configure HOME_NET and the appropriate network interface.
Validate the custom rules before monitoring authorized traffic.

Snort JSON output must be connected to the log path used by
alert_parser.py for live alerts.

## Security Testing
- Confirm the sample events appear in the dashboard.
- Validate local.rules using the installed Snort version.
- Generate benign traffic inside an authorized lab.
- Confirm matching rules generate alerts.
- Compare recorded Snort alerts with dashboard output.

## Limitations
The initial dashboard uses sample data. It does not capture packets
or detect intrusions by itself. Detection depends on Snort, the
selected rules, network visibility, and configuration.

## Educational Use
For a Network Security mini project and authorized lab testing.
