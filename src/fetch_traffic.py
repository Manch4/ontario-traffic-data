#made to fetch raw data from ontario 511 requests and write the data to file
import requests 
import json
from pathlib import Path
from datetime import datetime, timezone #imports for needed functions
url = "https://511on.ca/api/v2/get/event?format=json" #API endpoint for Ontario 511 traffic data 

response = requests.get(url) #reponse.get() will take some URL and return us the data at the adress here 

response.raise_for_status() #check if it worked

events = response.json() #events is an array of our traffic incidents derived from the 

timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S") #time formatting we can later use as a format to specify events 

output_dir = Path("data/raw") 
output_dir.mkdir(parents=True, exist_ok=True) #confirm that the folders exist for the next line

output_file = output_dir / f"traffic_events_{timestamp}.json" #creation of the output file sent to the data/raw folder with the timestamp as specifed name (directed by output_dir)

with open(output_file, "w", encoding="utf-8") as file:  
    json.dump(events, file, indent=2) 

print(f"Fetched {len(events)} traffic events.")
print(f"Raw data saved to: {output_file}")