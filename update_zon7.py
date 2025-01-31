from pathlib import Path
import os
import re

import contextlib


@contextlib.contextmanager
def CD(d):
    old = os.getcwd()
    os.chdir(d)
    yield

    os.chdir(old)


if __name__ == "__main__":
    import glob

    files = glob.glob("**/*.zon", recursive=True)
    for file in files:
        lines = []
        file = Path(file)
        content = file.read_text(encoding="utf8")
        for line in content.split("\n"):
            if ".path = " in line:
                content = re.findall(r'"(.*)"', line)[0]
                print(content)

                content2 = content[content.index("unzip/github.com") :]
                levels = str(file).replace("\\", "/").count("/")
                c2 = "../" * levels + content2
                line = line.replace(content, c2)

            lines.append(line)
        file.write_text("\n".join(lines), encoding="utf8")
