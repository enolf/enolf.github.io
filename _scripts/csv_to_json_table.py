import csv
import json
import os

# Configuration
CSV_FILE = 'assets/data/events/ea-events.csv'
JSON_OUTPUT = 'assets/data/events/ea-events-table.json'

def convert():
    if not os.path.exists(CSV_FILE):
        print(f"Error: {CSV_FILE} not found.")
        return

    data = []
    with open(CSV_FILE, mode='r', encoding='utf-8-sig') as f:
        # DictReader automatically uses the first row as keys
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)

    with open(JSON_OUTPUT, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
    
    print(f"Success: Created {JSON_OUTPUT} with {len(data)} rows.")

if __name__ == "__main__":
    convert()