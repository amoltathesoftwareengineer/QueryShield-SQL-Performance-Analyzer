
from src.report_generator import generate_html_report


def test_html_report_is_generated(tmp_path):
    analysis = {
        "risk_level": "HIGH",
        "risk_score": 3,
        "features": {
            "select_star": 1,
            "join_count": 3,
        },
        "recommendations": [
            "Review query execution plan."
        ],
    }

    output_file = tmp_path / "query_report.html"

    result = generate_html_report(analysis, output_file)

    assert output_file.exists()
    assert result == str(output_file)

    content = output_file.read_text(encoding="utf-8")
    assert "QueryShield" in content
    assert "HIGH" in content
    assert "Review query execution plan." in content


def test_html_report_escapes_untrusted_text(tmp_path):
    analysis = {
        "risk_level": "<script>alert(1)</script>",
        "risk_score": 1,
        "features": {},
        "recommendations": ["<b>Unsafe</b>"],
    }

    output_file = tmp_path / "safe_report.html"
    generate_html_report(analysis, output_file)

    content = output_file.read_text(encoding="utf-8")
    assert "<script>" not in content
    assert "&lt;script&gt;" in content
    assert "&lt;b&gt;Unsafe&lt;/b&gt;" in content
