
from flask import Flask, render_template
from alert_parser import parse_alerts

app = Flask(__name__)


@app.after_request
def security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["Content-Security-Policy"] = (
        "default-src 'self'; style-src 'self'; "
        "script-src 'self'; frame-ancestors 'none'"
    )
    response.headers["Cache-Control"] = "no-store"
    return response


@app.route("/")
def dashboard():
    alerts = parse_alerts()

    protocols = {}
    for alert in alerts:
        protocol = alert["protocol"].upper()
        protocols[protocol] = protocols.get(protocol, 0) + 1

    return render_template(
        "index.html",
        alerts=alerts,
        total_alerts=len(alerts),
        protocols=protocols,
    )


if __name__ == "__main__":
    # Local-only dashboard for the mini project.
    app.run(host="127.0.0.1", port=5000, debug=False)
