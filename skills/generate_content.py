from typing import Dict

def generate_content(input_data: Dict) -> Dict:
    content_type = input_data.get('type')
    if not content_type:
        raise ValueError("Type required")
    raise NotImplementedError("Not implemented")