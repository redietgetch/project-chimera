# tests/test_generate_content.py
import pytest
from skills.generate_content import generate_content

def test_generate_content_structure():
    result = generate_content({'type': 'video', 'prompt': 'Summer fashion promo'})
    assert isinstance(result, dict)
    assert 'content' in result
    assert 'type' in result
    assert 'confidence' in result
    assert isinstance(result['confidence'], float)
    assert 0 <= result['confidence'] <= 1