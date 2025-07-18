from pathlib import Path
from time import ctime
path = Path("python/01_variable.py")
path.exists()
# path.rename("new variable")
# path.unlink()

print(ctime(path.stat().st_ctime))

path.write_bytes()
path.read_bytes()
print(path)

