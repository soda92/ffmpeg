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
            if "git+" in line:
                print(line)
                repo = re.findall(r'(https://.*)"', line)[0]
                print(repo)

                url = repo.split("#")[0]
                hash = repo.split("#")[1]

                print(url, hash)

                target_dir = url.replace("https://", "unzip/")
                target_dir = Path(target_dir).resolve()
                target_dir.parent.mkdir(exist_ok=True, parents=True)

                with CD(target_dir.parent):
                    import subprocess

                    subprocess.run(["git", "clone", url])
                    with CD(target_dir):
                        subprocess.run(["git", "checkout", hash])

                line = line.replace(".url", ".path")
                line = line.replace(repo, url.replace("https://", "unzip/"))
                line = line.replace("git+", "")

            lines.append(line)
        content=  "\n".join(lines)
        content = "\n".join(filter(lambda x: ".hash" not in x, content.split("\n")))

        file.write_text(content, encoding="utf8")
