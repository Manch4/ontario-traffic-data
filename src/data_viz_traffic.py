import sqlite3 
from pathlib import Path 
import matplotlib.pyplot as plt #import to allow creation of charts 
 
 
# Connect to our traffic database 
database_file = Path("data/traffic.db") #set to pull from our traffic.db 
connection = sqlite3.connect(database_file) #connecting sqlite 
 
 
#1. Top 10 roads by traffic events Ontario 
query = """ 
SELECT 
    road, 
    COUNT(*) AS event_count 
FROM traffic_events 
WHERE road IS NOT NULL 
    AND road <> '' 
GROUP BY road 
ORDER BY event_count DESC 
LIMIT 10; 
""" 
 
results = connection.execute(query).fetchall()#query execution and gathers results under this variable 
 
roads = [row[0] for row in results] 
event_counts = [row[1] for row in results] #allows the roads/event count to be represented as chart data 
 
 
plt.figure(figsize=(10, 6)) 
plt.barh(roads[::-1], event_counts[::-1]) #creates bars using the roads and event count size 
 
plt.xlabel("Number of traffic events") 
plt.ylabel("Road") 
plt.title("Top 10 Ontario Roads by Traffic Events") #table titles  
 
plt.tight_layout() 
 
 
# Save the chart to the project 
output_file = Path("data/cleaned/top_10_roads.png") 
plt.savefig(output_file, dpi=300) #formatting for saving chart 
 
print(f"Chart saved to: {output_file}") 
 
 
# next chart # 
 
 
# 2. Top 10 events by number of events  
query = """ 
SELECT 
    event_type, 
    COUNT(*) AS event_count 
FROM traffic_events 
WHERE event_type IS NOT NULL 
    AND event_type <> '' 
GROUP BY event_type 
ORDER BY event_count DESC; 
""" 
 
results = connection.execute(query).fetchall() 
 
event_types = [row[0] for row in results] 
event_counts = [row[1] for row in results] #Order rows and columns 
 
plt.figure(figsize=(10, 6)) 
plt.barh(event_types[::-1], event_counts[::-1]) #Organize bars 
 
plt.xlabel("Number of traffic events") 
plt.ylabel("Event type") 
plt.title("Ontario Traffic Events by Type") #Lable titles 
 
plt.tight_layout() 
 
output_file = Path("data/cleaned/events_by_type.png") 
plt.savefig(output_file, dpi=300) #save project as png  
 
connection.close()  
 
print(f"Chart saved to: {output_file}")