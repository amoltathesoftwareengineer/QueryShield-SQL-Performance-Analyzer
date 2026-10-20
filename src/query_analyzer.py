
import re
from time import perf_counter


def analyze_query(query: str) -> dict:
    """Analyze basic SQL query features and estimate optimization risks."""
    if not isinstance(query, str) or not query.strip():
        raise ValueError("SQL query cannot be empty.")

    normalized = re.sub(r"\s+", " ", query.strip()).upper()

    features = {
        "query_length": len(query),
        "select_star": int(bool(re.search(r"\bSELECT\s+\*", normalized))),
        "join_count": len(re.findall(r"\bJOIN\b", normalized)),
        "where_present": int(bool(re.search(r"\bWHERE\b", normalized))),
        "group_by_present": int(bool(re.search(r"\bGROUP\s+BY\b", normalized))),
        "order_by_present": int(bool(re.search(r"\bORDER\s+BY\b", normalized))),
        "subquery_count": normalized.count("SELECT") - 1,
        "has_aggregation": int(
            bool(re.search(r"\b(COUNT|SUM|AVG|MIN|MAX)\s*\(", normalized))
        ),
    }

    score = 0
    recommendations = []

    if features["select_star"]:
        score += 1
        recommendations.append(
            "Select only the columns you need instead of SELECT *."
        )

    if features["join_count"] >= 3:
        score += 1
        recommendations.append(
            "Review joins and confirm that join keys are indexed where appropriate."
        )

    if not features["where_present"] and re.search(
        r"\b(SELECT|UPDATE|DELETE)\b", normalized
    ):
        score += 1
        recommendations.append(
            "Check whether filtering is required; avoid unintentionally processing all rows."
        )

    if features["order_by_present"]:
        score += 1
        recommendations.append(
            "Check whether sorting is necessary and whether an appropriate index can help."
        )

    if features["subquery_count"] > 0:
        recommendations.append(
            "Review the subquery and compare alternatives using the execution plan."
        )

    if not recommendations:
        recommendations.append(
            "Review the execution plan and benchmark with representative data."
        )

    risk_level = "LOW" if score <= 1 else "MEDIUM" if score <= 2 else "HIGH"

    return {
        "risk_score": score,
        "risk_level": risk_level,
        "features": features,
        "recommendations": recommendations,
    }


def benchmark_query(run_query, repetitions: int = 3) -> dict:
    """Benchmark a callable that executes a query; report elapsed wall time."""
    if repetitions < 1:
        raise ValueError("Repetitions must be at least 1.")

    timings = []

    for _ in range(repetitions):
        start = perf_counter()
        run_query()
        timings.append(perf_counter() - start)

    return {
        "repetitions": repetitions,
        "execution_times_seconds": timings,
        "average_seconds": sum(timings) / len(timings),
        "minimum_seconds": min(timings),
        "maximum_seconds": max(timings),
    }
