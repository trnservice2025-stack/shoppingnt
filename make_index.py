import os
from datetime import datetime

BASE_DIR = os.getcwd()


def make_index(current_dir, is_root=False):
    entries = []

    for name in os.listdir(current_dir):
        if name.startswith("."):
            continue

        full_path = os.path.join(current_dir, name)

        if os.path.isdir(full_path):
            entries.append(("dir", name, None))
        elif name.endswith(".html") and name != "index.html":
            mtime = os.path.getmtime(full_path)
            entries.append(("file", name, mtime))

    # 파일은 수정일 최신순, 폴더는 이름순
    dirs = sorted([e for e in entries if e[0] == "dir"], key=lambda x: x[1])
    files = sorted(
        [e for e in entries if e[0] == "file"],
        key=lambda x: x[2],
        reverse=True
    )

    title = "shoppingnt" if is_root else os.path.basename(current_dir)

    html = f"""<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<title>{title}</title>
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
.back {{
  margin-bottom: 16px;
}}
</style>
</head>
<body>
"""

    if not is_root:
        html += '<div class="back"><a href="../">← 상위 폴더</a></div>\n'

    html += f"<h1>{title}</h1><ul>\n"

    # 폴더 먼저
    for _, name, _ in dirs:
        html += f'<li><a href="{name}/">{name}/</a></li>\n'

    # 파일
    for _, name, mtime in files:
        date_str = datetime.fromtimestamp(mtime).strftime("%Y-%m-%d")
        html += f'''
<li>
  <a href="{name}">{name}</a>
  <span class="date">{date_str}</span>
</li>
'''

    html += """
</ul>
</body>
</html>
"""

    with open(os.path.join(current_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)

    print(f"✅ index.html 생성: {current_dir}")

    # 🔁 재귀: 하위 폴더에도 동일하게 실행
    for _, name, _ in dirs:
        make_index(os.path.join(current_dir, name))


# ▶ 실행 시작 (루트부터)
make_index(BASE_DIR, is_root=True)
