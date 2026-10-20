
# 🛡️ QueryShield — SQL Performance & Query Optimization Analyzer

A Python-based SQL analysis tool that identifies potential query optimization risks, extracts query features, provides optimization recommendations, benchmarks callable operations, and generates HTML analysis reports.

## 🚀 Features

- SQL query feature extraction
- Heuristic-based query risk scoring
- Optimization recommendations
- Query execution-time benchmarking through a Python callable
- HTML performance analysis report generation
- PostgreSQL sample schema and queries
- Automated tests with pytest
- GitHub Actions CI workflow

## 🧰 Technology Stack

- Python 3.12+
- SQL
- PostgreSQL
- pytest
- pandas (dependency)
- GitHub Actions
- HTML and CSS

## 📂 Project Structure

```text
QueryShield-SQL-Performance-Analyzer/
├── .github/
│   └── workflows/
│       └── python-tests.yml
├── src/
│   ├── __init__.py
│   ├── query_analyzer.py
│   └── report_generator.py
├── sql/
│   └── sample_queries.sql
├── tests/
│   ├── __init__.py
│   ├── test_query_analyzer.py
│   └── test_report_generator.py
├── requirements.txt
└── README.md
```

## ⚙️ Installation

```bash
git clone https://github.com/amoltathesoftwareengineer/QueryShield-SQL-Performance-Analyzer.git
cd QueryShield-SQL-Performance-Analyzer

python -m venv .venv
```

Activate the environment:

**Windows**
```bash
.venv\Scripts\activate
```

**Linux / macOS**
```bash
source .venv/bin/activate
```

Install dependencies and run tests:

```bash
pip install -r requirements.txt
python -m pytest -v
```

## 💻 Usage

```python
from src.query_analyzer import analyze_query

query = "SELECT * FROM employees"

result = analyze_query(query)

print("Risk Level:", result["risk_level"])
print("Risk Score:", result["risk_score"])
print("Features:", result["features"])
print("Recommendations:", result["recommendations"])
```

## 📊 Generate an HTML Report

```python
from src.query_analyzer import analyze_query
from src.report_generator import generate_html_report

query = "SELECT * FROM employees"

analysis = analyze_query(query)
report_path = generate_html_report(analysis)

print(f"Report generated: {report_path}")
```

The report is written to `reports/query_report.html` by default.

## 🗄️ PostgreSQL Sample Queries

Open `sql/sample_queries.sql` in a PostgreSQL SQL client and execute it in a development database to create the sample tables and run example queries.

Use PostgreSQL's `EXPLAIN` to inspect query plans. Use `EXPLAIN ANALYZE` only when you intend to execute the query and understand its effects.

## 🧪 Testing

Automated tests cover:

- Query feature detection
- Basic risk scoring
- Input validation
- Benchmark metrics
- HTML report generation
- HTML escaping

GitHub Actions runs the test suite on pushes and pull requests.

## ⚠️ Limitations

- Risk scores are heuristic indicators, not predictions from a trained model.
- Query runtime benchmarking requires a callable and does not automatically connect to PostgreSQL.
- Actual execution-plan parsing and index recommendation analysis are not yet implemented.
- pandas is listed as a dependency but is not currently required by the implemented core functions.
- The optional Streamlit dashboard is planned, not implemented.

## 🗺️ Roadmap

- [x] SQL query feature analysis
- [x] Heuristic risk scoring
- [x] Optimization recommendations
- [x] HTML report generation
- [x] Automated tests
- [x] GitHub Actions workflow
- [ ] PostgreSQL connection and execution-plan parser
- [ ] Index recommendation engine
- [ ] Interactive Streamlit dashboard

## 🔐 Safety

- Use a development database for experiments.
- Never commit database credentials or secrets.
- Review SQL statements before execution.
- Benchmark queries using comparable data and conditions.

## 📄 License

MIT License. See [LICENSE](LICENSE) for details.
