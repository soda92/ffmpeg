import glob
from pathlib import Path
import subprocess

CURRENT = Path(__file__).resolve().parent

gz_files = glob.glob("**/*.tar.gz", recursive=True, root_dir=CURRENT.joinpath("tmp"))

for file in gz_files:
    target_dir = CURRENT.joinpath("unzip").joinpath(file)
    orig_file = CURRENT.joinpath("tmp").joinpath(file)

    print(orig_file)
    print(target_dir)

    target_dir.parent.mkdir(exist_ok=True, parents=True)

    subprocess.run(["tar", "xf", orig_file, "-C", target_dir.parent])
