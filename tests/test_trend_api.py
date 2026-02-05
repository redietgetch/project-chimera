import json
from datetime import datetime

# Example Trend Fetch API input
trend_input = {
    "platform": "tiktok",
    "region": "global"
}

# Fake function to simulate Trend Fetch API
def fetch_trends(input_data):
    """
    Simulates Trend Fetch API based on Technical Spec.
    Returns JSON structured output.
    """
    platform = input_data.get("platform")
    region = input_data.get("region")

    # Example static output (replace with real API later)
    trends = [
        {"topic": "AI Influencers", "score": 95, "source": platform},
        {"topic": "Short Video Marketing", "score": 87, "source": platform},
        {"topic": "Viral Challenges", "score": 80, "source": platform}
    ]

    return {
        "trends": trends,
        "fetched_at": datetime.utcnow().isoformat() + "Z"
    }

# Call the function with the input
output = fetch_trends(trend_input)

# Pretty print the JSON output
print(json.dumps(output, indent=4))
