# Simulate file streaming by placing batch files into q4_sensor_data
# Read original data from /shared/midterm/q4_sensor_data.json
# cp q4_sensor_data_chunked/batch_2.json q4_sensor_data/
import json
import shutil
import time

# Read original JSON data
with open("shared/midterm/q4_sensor_data.json") as f:
    lines = f.readlines()

# Split into chunks of 50 lines each
chunk_size = 50
for i in range(0, len(lines), chunk_size):
    chunk = lines[i:i+chunk_size]
    with open(f"q4_sensor_data/batch_{i//chunk_size+1}.json", "w") as f_out:
        f_out.writelines(chunk)
    time.sleep(20)
    
