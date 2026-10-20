
import pytest

from src.query_analyzer import analyze_query, benchmark_query


def test_select_star_is_flagged():
    result = analyze_query("SELECT * FROM employees")
    assert result["features"]["select_star"] == 1
    assert result["risk_score"] >= 1


def test_where_clause_is_detected():
    result = analyze_query(
        "SELECT employee_id FROM employees WHERE employee_id = 10"
    )
    assert result["features"]["where_present"] == 1


def test_join_count_is_detected():
    result = analyze_query(
        "SELECT a.id FROM a JOIN b ON a.id = b.id "
        "JOIN c ON b.id = c.id JOIN d ON c.id = d.id"
    )
    assert result["features"]["join_count"] == 3


def test_aggregation_is_detected():
    result = analyze_query("SELECT COUNT(*) FROM employees")
    assert result["features"]["has_aggregation"] == 1


def test_empty_query_raises_error():
    with pytest.raises(ValueError):
        analyze_query("")


def test_benchmark_returns_metrics():
    result = benchmark_query(lambda: sum(range(100)), repetitions=2)
    assert result["repetitions"] == 2
    assert len(result["execution_times_seconds"]) == 2
    assert result["average_seconds"] >= 0


def test_invalid_repetitions_raise_error():
    with pytest.raises(ValueError):
        benchmark_query(lambda: None, repetitions=0)
