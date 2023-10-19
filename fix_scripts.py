import sys
from pathlib import Path

for script in Path("Scripts").glob("*.exe"):
    print("Rewriting", script)
    data = script.read_bytes()
    data = data.replace(sys.prefix.encode(), b".")
    script.write_bytes(data)

for pth in Path().glob("*._pth"):
    print("Enabling site in", pth)
    data = pth.read_bytes()
    data = data.replace(b"#import site", b"import site")
    pth.write_bytes(data)
