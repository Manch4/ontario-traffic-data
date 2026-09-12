import subprocess
import sys


# Run the complete traffic data pipeline (run from here)
steps = [
    "src/fetch_traffic.py",
    "src/clean_traffic.py",
    "src/load_to_database",
    "src/data_viz_traffic.py"
]


for script in steps:
    subprocess.run([sys.executable, script], check=True) #runs steps as needed


print("\nPipeline completed successfully.")