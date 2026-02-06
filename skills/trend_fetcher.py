from typing import Dict

def fetch_trends(input_data: Dict) -> Dict:
    query = input_data.get('query')
    if not query:
        raise ValueError("Query required")
    raise NotImplementedError("Not implemented")