import os
from datetime import datetime

BASE_DIR = os.getcwd()

def make_index(target_dir):
    files = []

    for name in os.listdir(target_dir):
        if name.endswith(".html") and name != "index.html":
            full_path = os.path.join(target_dir, name)
            mtime = os.path.getmtime(full_path)
            files.append((name, mtime))

    # 🔹 수정일 최신순 정렬
    files.sort(key=lambda x: x[1], reverse=True)

    html = f"""<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<title>{os.path.basename(target_dir)} 목록</title>
<style>
body {{
  font-family: system-ui, -apple-system, sans-serif;
  padding: 24px;
}}
ul {{
  list-style: none;
  padding: 0;
}}
li {{
  display: flex;
  justify-content: space-between;
  padding: 6px 0;
  border-bottom: 1px solid #eee;
}}
.date {{
  color: #666;
  font-size: 0.9em;
}}
</style>
</head>
<body>

<h1>{os.path.basename(target_dir)}</h1>
<ul>
"""

    for filename, mtime in files:
        date_str = datetime.fromtimestamp(mtime).strftime("%Y-%m-%d")
        html += f'''
<li>
  <a href="{filename}">{filename}</a>
  <span class="date">{date_str}</span>
</li>
'''

    html += """
</ul>
</body>
</html>
"""

    with open(os.path.join(target_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)

    print(f"✅ {target_dir}/index.html 생성 완료")


# 🔥 여러 폴더 자동 처리
for item in os.listdir(BASE_DIR):
    path = os.path.join(BASE_DIR, item)
    if os.path.isdir(path) and not item.startswith("."):
        make_index(path)