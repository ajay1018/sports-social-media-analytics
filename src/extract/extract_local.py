from pathlib import Path
import json
RAW = Path("data/raw"); RAW.mkdir(parents=True, exist_ok=True)
src = RAW / "posts.json"
# in a real project, fetch from API; here we just confirm the file exists
posts = json.loads(src.read_text(encoding="utf-8"))
print(f"[extract] posts: {len(posts)} -> {src}")
