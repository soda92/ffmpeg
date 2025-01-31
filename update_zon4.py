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
            if ".path = " in line and "archive" in line:
                # unzip/github.com/allyourcodebase/libressl/archive/refs/tags/3.9.2+1
                # to: unzip/github.com/allyourcodebase/libressl/archive/refs/tags/libressl-3.9.2+1
                pass
                content = re.findall(r'"(.*)"', line)[0]
                if "\\" in line:
                    print(line)
                paths = content.split("/")
                repo_name = paths[3]
                if paths[-1].startswith("v"):
                    paths[-1] = paths[-1][1:]
                if repo_name not in paths[-1]:
                    paths[-1] = f"{repo_name}-{paths[-1]}"

                d = "/".join(paths)
                lines.append(line.replace(content, d))

                if not Path(d).exists():
                    print(file, content, d)
            else:
                lines.append(line)
        file.write_text("\n".join(lines), encoding="utf8")
