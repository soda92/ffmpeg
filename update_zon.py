from pathlib import Path
import re
import subprocess
import glob

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

CURRENT = Path(__file__).resolve().parent

gz_files = glob.glob("**/*.tar.gz", recursive=True, root_dir=CURRENT.joinpath("tmp"))

for file in gz_files:
    target_dir = CURRENT.joinpath("unzip").joinpath(file)
    orig_file = CURRENT.joinpath("tmp").joinpath(file)

    print(orig_file)
    print(target_dir)

    target_dir.parent.mkdir(exist_ok=True, parents=True)

    subprocess.run(["tar", "xf", orig_file, "-C", target_dir.parent])


CURRENT = Path(__file__).resolve().parent
content = CURRENT.joinpath("build.zig.zon").read_text(encoding="utf8")

urls = re.findall(r'(.url = "https.*\.tar.gz")', content)

print(urls)

for i in urls:
    p = i.replace("https://", "unzip/").replace(".url", ".path").replace(".tar.gz", "")
    content = content.replace(i, p)

content = "\n".join(filter(lambda x: ".hash" not in x, content.split("\n")))
CURRENT.joinpath("build.zig.zon").write_text(content, encoding="utf8")
