# Skills Directory

This directory contains reusable "skills" for Chimera Agents.

## Skill List

### 1. Fetch Trends (fetch_trends.py)
- Purpose: Poll for trends.
- Input: dict with 'query' (str).
- Output: dict with 'trends' (list).

### 2. Generate Content (generate_content.py)
- Purpose: Generate multimodal content.
- Input: dict with 'type' (str), 'prompt' (str).
- Output: dict with 'content' (str or URL).

### 3. Publish Video (publish_video.py)
- Purpose: Publish to social platforms.
- Input: dict with 'platform' (str), 'video_url' (str).
- Output: dict with 'post_id' (str).