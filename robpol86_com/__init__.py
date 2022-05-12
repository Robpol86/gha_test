"""Robpol86.com."""
from pathlib import Path

__author__ = "@Robpol86"
__license__ = "BSD-2-Clause"
__version__ = __import__("pkg_resources").get_distribution(__name__).version


# Assert version is listed in changelog (reminder: not suitable for public libraries).
with (Path(__file__).parent.parent / "CHANGELOG.md").open("r", encoding="utf8") as __F:
    __LINE = ""
    for __LINE in (__L.rstrip() for __L in __F):
        if __LINE.startswith("## [2"):
            break
    if __LINE != f"## [{__version__}]":
        raise RuntimeError(f"{__LINE!r} != '## [{__version__}]'")
    del __LINE
del __F
