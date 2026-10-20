
from html import escape
from pathlib import Path


def generate_html_report(analysis: dict, output_path="reports/query_report.html"):
    """Generate a simple HTML report from QueryShield analysis results."""

    features = analysis.get("features", {})
    recommendations = analysis.get("recommendations", [])

    feature_rows = "".join(
        f"<tr><td>{escape(str(name))}</td>"
        f"<td>{escape(str(value))}</td></tr>"
        for name, value in features.items()
    )

    recommendation_items = "".join(
        f"<li>{escape(str(item))}</li>"
        for item in recommendations
    )

    risk_level = escape(str(analysis.get("risk_level", "UNKNOWN")))
    risk_score = escape(str(analysis.get("risk_score", "N/A")))

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>QueryShield SQL Analysis Report</title>
<style>
body {{ font-family: Arial, sans-serif; max-width: 900px;
       margin: 40px auto; padding: 20px; color: #222; }}
h1 {{ color: #174ea6; }}
table {{ border-collapse: collapse; width: 100%; }}
th, td {{ border: 1px solid #ddd; padding: 10px; text-align: left; }}
th {{ background: #f2f5fa; }}
.risk {{ font-size: 1.2rem; font-weight: bold; }}
</style>
</head>
<body>
<h1>QueryShield</h1>
<h2>SQL Performance Analysis Report</h2>
<p class="risk">Risk Level: {risk_level}</p>
<p>Risk Score: {risk_score}</p>
<h2>Query Features</h2>
<table>
<thead><tr><th>Feature</th><th>Value</th></tr></thead>
<tbody>{feature_rows}</tbody>
</table>
<h2>Recommendations</h2>
<ul>{recommendation_items}</ul>
<p><em>Risk scores are heuristic indicators, not measured query performance.</em></p>
</body>
</html>
"""

    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(html, encoding="utf-8")
    return str(path)
