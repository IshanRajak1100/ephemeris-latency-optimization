import csv
import datetime
from pathlib import Path
import math

# ---- paths ----
BASE_DIR = Path(__file__).resolve().parents[2]
timestamps_path = BASE_DIR / "data" / "raw" / "timestamps.txt"
positions_path = BASE_DIR / "data" / "raw" / "position.csv"  # keep this filename as you requested

# ---- one query to test ----
example = datetime.datetime(2014, 1, 5, 00, 0, 0, tzinfo=datetime.timezone.utc)

# ---- helpers ----
def moon_position(ts: datetime.datetime) -> tuple[float, float, float]:
    t = ts.timestamp()  # correct method name
    return (t * 1e-6, t * 1e-6, -t * 1e-6)

def distance(a: tuple[float, float, float], b: tuple[float, float, float]) -> float:
    return math.sqrt(
        (a[0] - b[0]) ** 2 +
        (a[1] - b[1]) ** 2 +
        (a[2] - b[2]) ** 2
    )

# ---- load timestamps ----
timestamps: list[datetime.datetime] = []
with timestamps_path.open("r") as f:
    for line in f:
        ts = datetime.datetime.strptime(line.strip(), "%Y-%m-%d %H:%M:%S").replace(
            tzinfo=datetime.timezone.utc
        )
        timestamps.append(ts)

# ---- baseline 1 timestamp ----
past = [t for t in timestamps if t <= example]
if not past:
    raise ValueError("No past timestamp — fallback required")

baseline_ts = max(past)

# ---- load positions ----
positions: list[tuple[datetime.datetime, float, float, float]] = []
with positions_path.open("r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        ts = datetime.datetime.fromisoformat(row["timestamp"]).replace(tzinfo=datetime.timezone.utc)
        x = float(row["x"])
        y = float(row["y"])
        z = float(row["z"])
        positions.append((ts, x, y, z))

# ---- map baseline timestamp -> baseline position ----
baseline_position = next((p for p in positions if p[0] == baseline_ts), None)
if baseline_position is None:
    raise ValueError("Baseline timestamp not found in position.csv (timestamps/positions misaligned)")

# ---- compute error for one query ----
true_pos = moon_position(example)
baseline_pos = baseline_position[1:]
err = distance(true_pos, baseline_pos)

print("Query time:", example)
print("Baseline timestamp:", baseline_ts)
print("True position:", true_pos)
print("Baseline position:", baseline_pos)
print("Baseline-1 error:", err)
