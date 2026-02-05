import csv
import datetime
from pathlib import Path


timestamps=[]

BASE_DIR = Path(__file__).resolve().parents[2]
timestamps_path = BASE_DIR / "data" / "raw" / "timestamps.txt"

with timestamps_path.open("r") as f:
    for line in f:
        ts = datetime.datetime.strptime(line.strip(), "%Y-%m-%d %H:%M:%S")
        timestamps.append(ts)
        
        
def moon_position(ts: datetime.datetime)->tuple[float, float,float]:
    # Placeholder for actual moon position calculation
    
    t = ts.timestamp()
    x = t * 1e-6
    y = t * 1e-6
    z = -t * 1e-6
    return (x, y, z)

positions_path = BASE_DIR / "data" / "raw" / "position.csv"

if positions_path.exists():
    print(f"{positions_path} already exists. Skipping position generation.")
    

with positions_path.open("w",newline="\n") as f:
    writer = csv.writer(f)
    writer.writerow(["timestamp", "x", "y", "z"])
    for ts in timestamps:
        
        x, y, z = moon_position(ts)
        # isoformat() converts the datetime to a string in ISO 8601 format
        writer.writerow([ts.isoformat(), x, y, z])
        
   
   
print(f"rows written: {len(timestamps)}")
print("first timestamp:", timestamps[0])
print("last timestamp:", timestamps[-1])
print("output file:", positions_path)
    