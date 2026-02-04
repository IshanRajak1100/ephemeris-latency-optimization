
from datetime import datetime, timedelta
from pathlib import Path
start_date = datetime(2014, 1, 1)
end_date = datetime(2025, 12, 31)
gap = 6 #hours

current_date = start_date
output_path = Path("../../data/raw/timestamps.txt")
output_path.parent.mkdir(parents=True, exist_ok=True)

with output_path.open("w") as f:
    while current_date <= end_date:
        f.write(current_date.strftime("%Y-%m-%d %H:%M:%S") + "\n")
        current_date += timedelta(hours=gap)
        
        
        
        