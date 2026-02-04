import datetime
from pathlib import Path


timestamps=[]

BASE_DIR = Path(__file__).resolve().parents[2]
timestamps_path = BASE_DIR / "data" / "raw" / "timestamps.txt"

with timestamps_path.open("r") as f:
    for line in f:
        ts = datetime.datetime.strptime(line.strip(), "%Y-%m-%d %H:%M:%S")
        timestamps.append(ts)
        
        