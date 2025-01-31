import subprocess
from pathlib import Path
import send2trash

if Path("tmp").exists():
    # send2trash.send2trash("tmp")
    pass
if Path("unzip").exists():
    send2trash.send2trash("unzip")
subprocess.run(["git", "restore", "build.zig.zon"])
subprocess.run(["python", "update_zon.py"])
subprocess.run(["python", "update_zon2.py"])
subprocess.run(["python", "update_zon3.py"])
subprocess.run(["python", "update_zon2.py"])
subprocess.run(["python", "update_zon4.py"])
subprocess.run(["python", "update_zon5.py"])
subprocess.run(["python", "update_zon6.py"])
