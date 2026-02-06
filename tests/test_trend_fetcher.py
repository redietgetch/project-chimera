import pytest
from skills.trend_fetcher import fetch_trends

def test_fetch_trends_structure():
    # Test based on specs/technical.md: API Contract for Trends
    result = fetch_trends({'query': "fashion trends Ethiopia"})
    
    assert isinstance(result, dict), "Result must be a dictionary"
    assert "trends" in result, "Missing 'trends' key"
    assert isinstance(result["trends"], list), "'trends' must be a list"
    assert len(result["trends"]) > 0, "Trends list should not be empty"
    
    first_trend = result["trends"][0]
    assert "topic" in first_trend, "Each trend missing 'topic' key"
    assert isinstance(first_trend["topic"], str), "'topic' must be a string"
    assert "relevance" in first_trend, "Each trend missing 'relevance' key"
    assert isinstance(first_trend["relevance"], float), "'relevance' must be a float"
    assert first_trend["relevance"] > 0.5, "Relevance score too low per spec"

def test_fetch_trends_invalid_query():
    # Edge case from functional.md: Handle invalid queries gracefully
    with pytest.raises(ValueError):
        fetch_trends({'query': ""})