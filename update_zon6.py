from pathlib import Path
import os

import contextlib


@contextlib.contextmanager
def CD(d):
    old = os.getcwd()
    os.chdir(d)
    yield

    os.chdir(old)


if __name__ == "__main__":
    import glob

    files = glob.glob("**/*.zig", recursive=True)
    for file in files:
        lines = []
        file = Path(file)
        content = file.read_text(encoding="utf8")
        for line in content.split("\n"):
            if (
                "defineCMacro" in line
                and "LibreSslCommon, name: []" not in line
                and "defineCMacroForLibs" not in line
            ):
                print(line)
                line = line.replace("defineCMacro", "root_module.addCMacro")
                line = line.replace("null", '""')
                line = line.replace("libressl_common.root_module", "libressl_common.libcrypto.root_module")
                line = line.replace("value: ?[]const u8) void", "value: []const u8) void")
                lines.append(line)
            else:
                lines.append(line)
        file.write_text("\n".join(lines))
