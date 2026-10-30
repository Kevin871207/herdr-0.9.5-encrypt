import base64, glob, hashlib
from pathlib import Path

print("解碼中...")
parts = sorted(glob.glob("part_*.txt"))
enc = "".join(open(p).read() for p in parts).replace("\n", "")
data = base64.b85decode(enc)
expected, source_name = open("app.sha256").read().split(maxsplit=1)
output_name = Path(source_name.strip()).name
open(output_name, "wb").write(data)
print("OK" if hashlib.sha256(data).hexdigest() == expected else "雜湊不符!")
