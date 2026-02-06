import pytest
from skills.fetch_trends import fetch_trends
from skills.generate_content import generate_content
from skills.publish_video import publish_video

def test_skill_interface_compliance():
    # Test fetch_trends
    result = fetch_trends({'query': "test"})
    assert isinstance(result, dict)

    # Test generate_content
    result = generate_content({'type': "video"})
    assert isinstance(result, dict)

    # Test publish_video
    result = publish_video({'platform': "instagram"})
    assert isinstance(result, dict)