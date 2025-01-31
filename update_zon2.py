from pathlib import Path
import re
import subprocess

CURRENT = Path(__file__).resolve().parent


def unpack(gz_file: str, target_dir):
    target_dir.parent.mkdir(exist_ok=True, parents=True)

    subprocess.run(["tar", "xf", gz_file, "-C", target_dir.parent])


def update_zon(file: Path):
    content = file.read_text(encoding="utf8")

    urls = re.findall(r'.url = "(https.*\.tar.gz)"', content)

    print(urls)

    for i in urls:
        p = i.replace("https://", "tmp/")
        target_dir = Path(i.replace("https://", "unzip/")).parent
        p = CURRENT.joinpath(p)
        p.parent.mkdir(parents=True, exist_ok=True)
        # print(p)

        subprocess.run(["wget", i, "-O", str(p)], check=True)
        unpack(str(p), target_dir)


def update_zon2(zon: Path):
    content = zon.read_text(encoding="utf8")

    urls = re.findall(r'(.url = "https.*\.tar.gz")', content)

    print(urls)

    for i in urls:
        p = (
            i.replace("https://", "unzip/")
            .replace(".url", ".path")
            .replace(".tar.gz", "")
        )
        content = content.replace(i, p)

    content = "\n".join(filter(lambda x: ".hash" not in x, content.split("\n")))
    zon.write_text(content, encoding="utf8")


if __name__ == "__main__":
    import glob

    files = glob.glob("unzip/**/*.zon", recursive=True)
    for file in files:
        print(file)
        file = Path(file)
        update_zon(file)
        update_zon2(file)
