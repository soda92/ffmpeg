from pathlib import Path


def replace(s):
    s0, s1, s2 = s.split()
    c = Path(s0).read_text(encoding="utf8")
    s2 = Path(s2).relative_to(Path(s0)).replace("\\", "/")
    c = c.replace(s1, s2)
    Path(s0).write_text(c, encoding="utf8")


replace(
    "build.zig.zon unzip/github.com/allyourcodebase/libressl/archive/refs/tags/libressl-3.9.2+1 unzip/github.com/allyourcodebase/libressl/archive/refs/tags/libressl-3.9.2-1"
)

replace(
    r"unzip\github.com\allyourcodebase\mbedtls\build.zig.zon unzip/github.com/Mbed-TLS/mbedtls/archive/refs/tags/mbedtls-3.6.1 unzip/github.com/Mbed-TLS/mbedtls/archive/refs/mbedtls-mbedtls-3.6.1"
)

replace(
    r"unzip\github.com\allyourcodebase\zlib\archive\refs\tags\zlib-1.3.1-3\build.zig.zon unzip/github.com/madler/zlib/archive/refs/tags/zlib-1.3 unzip/github.com/madler/zlib/archive/refs/zlib-1.3 "
)
