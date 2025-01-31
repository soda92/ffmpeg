from pathlib import Path
import re
import subprocess

CURRENT = Path(__file__).resolve().parent
content = CURRENT.joinpath("build.zig.zon").read_text(encoding="utf8")

urls = re.findall(r'.url = "(https.*\.tar.gz)"', content)

print(urls)

for i in urls:
    p = i.replace("https://", "tmp/")
    p = CURRENT.joinpath(p)
    p.parent.mkdir(parents=True, exist_ok=True)
    # print(p)

    subprocess.run(["wget", i, "-O", str(p)], check=True)
