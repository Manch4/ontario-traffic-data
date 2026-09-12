# Ontario Traffic Data Pipeline

A Python-based ETL pipeline that collects current traffic-event data from the Ontario 511 API, cleans the data, stores it in a SQLite database, and generates charts for analysis.

## What This Project Does

The pipeline follows this process:

Ontario 511 API → Fetch → Clean → SQLite Database → SQL Analysis → Charts

When the pipeline is run, it:

1. Fetches the current traffic events available from Ontario 511.
2. Saves the raw API response as a timestamped JSON file.
3. Cleans the raw data and selects the relevant fields.
4. Loads the cleaned data into a SQLite database.
5. Generates charts from the collected data.

## Project Structure

    ontario-traffic-data-pipeline/
    │
    ├── data/
    │   ├── raw/
    │   ├── cleaned/
    │   │   ├── traffic_events_cleaned.json
    │   │   ├── top_10_roads.png
    │   │   └── events_by_type.png
    │   └── traffic.db
    │
    ├── src/
    │   ├── fetch_traffic.py
    │   ├── clean_traffic.py
    │   ├── load_to_database
    │   ├── analyze_traffic.sql
    │   └── data_viz_traffic.py
    │
    ├── run_traffic_pipeline.py
    ├── .gitignore
    └── README.md

## Requirements

You need:

- Python 3
- Internet access
- The Python packages `requests` and `matplotlib`

SQLite is included with Python and does not need to be installed separately.

## Setup

### 1. Clone the repository

Clone this repository to your computer and open the project folder in a terminal.

### 2. Create a virtual environment

From the project root folder, run:

    py -m venv .venv

### 3. Activate the virtual environment

On Windows PowerShell, run:

    .\.venv\Scripts\Activate.ps1

After activation, `(.venv)` should appear at the beginning of the terminal line.

### 4. Install the required packages

Run:

    pip install requests matplotlib

## Running the Pipeline

Make sure the terminal is in the project root folder, where `run_traffic_pipeline.py` is located.

Run:

    python run_traffic_pipeline.py

This single command runs the entire pipeline in order:

1. Fetch traffic data from Ontario 511
2. Clean the data
3. Store the data in SQLite
4. Generate the charts

You do not need to manually run each script in the `src` folder.

### If `python` does not work

On some Windows installations, the `python` command may not be configured correctly.

Try:

    py run_traffic_pipeline.py

If you are using the project's virtual environment and need to run Python directly, use:

    .\.venv\Scripts\python.exe run_traffic_pipeline.py

## Output

After a successful run, the project produces the following outputs.

### Raw Data

Location:

    data/raw/

Each API pull is saved as a separate timestamped JSON file.

The raw files are preserved so that different API pulls can be collected over time.

### Cleaned Data

Location:

    data/cleaned/traffic_events_cleaned.json

This contains the selected and cleaned fields used by the database.

### SQLite Database

Location:

    data/traffic.db

The database contains the `traffic_events` table.

### Charts

Location:

    data/cleaned/

The pipeline generates:

- `top_10_roads.png` — Top 10 roads by number of traffic events
- `events_by_type.png` — Traffic events grouped by event type

## SQL Analysis

SQL analysis is stored in:

    src/analyze_traffic.sql

The current queries analyze:

- Total number of traffic events
- Traffic events by event type
- Roads with the most traffic events
- Traffic events by direction
- Full closures vs. non-full closures

The SQL queries operate on the `traffic_events` table in `data/traffic.db`.

## Understanding the Data

The Ontario 511 API provides current traffic-event information when the API is requested.

This means each pipeline run collects the traffic events that are available from Ontario 511 at that time.

The project does not request a specific historical time range from the API.

Individual events can contain information such as:

- Road
- Description
- Direction
- Event type
- Reported time
- Last updated time
- Start date
- Planned end date
- Lanes affected
- Latitude and longitude
- Full-closure status
- Severity

Because raw API responses are saved with timestamps, repeatedly running the pipeline can begin building a historical collection of Ontario 511 API snapshots.

## Database Behaviour

The cleaned JSON file is overwritten each time the cleaning process runs.

The raw JSON files are not overwritten. Each API pull is saved separately.

The SQLite database uses the traffic event ID as the primary key.

When the pipeline encounters an event that already exists in the database, its information is updated. New events are added.

Events that are no longer returned by a later API pull are not automatically removed from the database.

Therefore, the database is currently a collection of traffic events encountered by the pipeline rather than an exact snapshot of the current Ontario 511 API.

## Data Source

Traffic data is provided by Ontario 511.

Ontario 511 API documentation:

https://511on.ca/developers/doc

## Technologies Used

- Python
- Requests
- SQLite
- SQL
- Matplotlib
- Ontario 511 API

## Pipeline Overview

    Ontario 511 API
           │
           ▼
    fetch_traffic.py
           │
           ▼
    data/raw/
           │
           ▼
    clean_traffic.py
           │
           ▼
    traffic_events_cleaned.json
           │
           ▼
    load_to_database
           │
           ▼
    data/traffic.db
           │
           ├───────────────┐
           ▼               ▼
    SQL Analysis     Visualization
                           │
                           ▼
                         Charts
