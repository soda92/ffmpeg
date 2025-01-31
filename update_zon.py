from pathlib import Path
import re
import subprocess

CURRENT = Path(__file__).resolve().parent
content = CURRENT.joinpath("build.zig.zon").read_text(encoding="utf8")

urls = re.findall(r'(.url = "https.*\.tar.gz")', content)

print(urls)

for i in urls:
    p = i.replace("https://", "unzip/").replace(".url", ".path").replace(".tar.gz", "")
    content = content.replace(i, p)

content = "\n".join(filter(lambda x: ".hash" not in x, content.split("\n")))
CURRENT.joinpath("build.zig.zon").write_text(content, encoding="utf8")
