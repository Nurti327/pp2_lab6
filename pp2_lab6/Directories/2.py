import os
from pathlib import Path
p = Path("lab_tmp")
print({
    "exists": p.exists(),
    "readable": os.access(p, os.R_OK),
    "writable": os.access(p, os.W_OK),
    "executable": os.access(p, os.X_OK),
})