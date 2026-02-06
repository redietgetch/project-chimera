# tests/test_publish_video.py
import pytest
from skills.publish_video import publish_video

def test_publish_video_structure():
    result = publish_video({'platform': 'instagram', 'video_url': 'example.mp4'})
    assert isinstance(result, dict)
    assert 'post_id' in result
    assert 'status' in result
    assert result['status'] in ['success', 'error']
    assert 'url' in result