import datetime
from pathlib import Path




example = datetime.datetime(2015,2,1,15,00,00)

BASE_DIR = Path(__file__).resolve().parents[2]
timestamps_path = BASE_DIR / "data" / "raw" / "timestamps.txt"

timestamps = []
with timestamps_path.open("r") as f:
    for line in f:
        ts = datetime.datetime.strptime(line.strip(), "%Y-%m-%d %H:%M:%S")
        timestamps.append(ts)
        

past = [t for t in timestamps if t <= example]

if not past:
    raise ValueError("No past timestamp — fallback required")
        
baseline_ts = max(past)
print("Baseline timestamp:", baseline_ts)
       
       