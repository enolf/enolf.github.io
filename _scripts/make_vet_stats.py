import json
import re
import random

def slugify(text):
    # If 'text' is a list (the culprit!), take the first item
    if isinstance(text, list):
        text = text[0]
    
    # Ensure it's a string, lowercase it, and swap spaces for hyphens
    text = str(text).lower().strip()
    return re.sub(r'\s+', '-', text)

# 1. Load the GeoJSON
geojson_path = 'assets/maps/cairnsRegionSuburbs.json'
with open(geojson_path, 'r') as f:
    geojson_data = json.load(f)

# 2. Setup for Mock Data
months = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
mock_stats = {}
new_features = []

# 3. Process & Reorder
for feature in geojson_data['features']:
    # Grab the name, defaulting to 'unknown' if missing
    raw_name = feature['properties'].get('name', 'unknown')
    
    # Clean it up into a string ID
    clean_id = slugify(raw_name)
    
    # Update properties and REORDER: Put properties before geometry
    new_props = feature['properties'].copy()
    new_props['suburb_id'] = clean_id
    
    ordered_feature = {
        "type": "Feature",
        "properties": new_props,
        "geometry": feature.get("geometry")
    }
    new_features.append(ordered_feature)
    
    # 4. Generate Mock Stats using the string ID as the key
    # (Since clean_id is now definitely a string, no more TypeError!)
    monthly_data = {}
    for m in months:
        if m in ["oct", "nov", "dec", "jan"]:
            monthly_data[m] = random.randint(10, 35) # Tick Season
        else:
            monthly_data[m] = random.randint(0, 5)
    
    mock_stats[clean_id] = monthly_data

# 5. Save the Reordered GeoJSON
geojson_data['features'] = new_features
with open(geojson_path, 'w') as f:
    json.dump(geojson_data, f, indent=4)

# 6. Save the Mock Stats
with open('assets/data/tick-stats.json', 'w') as f:
    json.dump(mock_stats, f, indent=4)

print(f"Success! Processed {len(new_features)} suburbs.")
print("GeoJSON reordered and 'tick-stats.json' generated without errors.")