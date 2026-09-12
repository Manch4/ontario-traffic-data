#clean  data from the derived api json file into a cleaner format
import json
from pathlib import Path

raw_dir = Path("data/raw") #where data is coming from

clean_dir = Path("data/cleaned")
clean_dir.mkdir(parents=True, exist_ok=True) #confirm folder present 

raw_files = sorted(raw_dir.glob("traffic_events_*.json")) #this will look at match the files from the raw data folder to this raw_files variable 

if not raw_files:
    raise FileNotFoundError("No  traffic data found.") #ensures that raw data folder is not blank

latest_file = raw_files[-1] #reads from last file (most recent)

with open(latest_file, "r", encoding="utf-8") as file: #reading files
    events = json.load(file)

cleaned_events = []

for event in events: #runs for lenght of events creates cleaner format then appends it to cleaned_events through append
    cleaned_event = {
        "id": event.get("ID"),
        "road": event.get("RoadwayName"),
        "description": event.get("Description"),
        "event_type": event.get("EventType"),
        "event_subtype": event.get("EventSubType"),
        "direction": event.get("DirectionOfTravel"),
        "reported": event.get("Reported"),
        "last_updated": event.get("LastUpdated"),
        "start_date": event.get("StartDate"),
        "planned_end_date": event.get("PlannedEndDate"),
        "lanes_affected": event.get("LanesAffected"),
        "latitude": event.get("Latitude"),
        "longitude": event.get("Longitude"),
        "is_full_closure": event.get("IsFullClosure"),
        "severity": event.get("Severity"),
    }

    cleaned_events.append(cleaned_event)

output_file = clean_dir / "traffic_events_cleaned.json" #creates the file we will be writing cleaned_events to

with open(output_file, "w", encoding="utf-8") as file: #formatting and writing to the file 
    json.dump(cleaned_events, file, indent=2)

print(f"Cleaned {len(cleaned_events)} traffic events.")
print(f"Cleaned data saved to: {output_file}")