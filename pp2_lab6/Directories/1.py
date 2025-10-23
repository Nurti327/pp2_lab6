from pathlib import Path
p = Path("lab_tmp")
dirs = sorted([e.name for e in p.iterdir() if e.is_dir()])
files = sorted([e.name for e in p.iterdir() if e.is_file()])
all_entries = sorted([e.name for e in p.iterdir()])
print("Dirs:", dirs)
print("Files:", files)
print("All:", all_entries)