import pandas as pd
import folium
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter

# Define a list of potential encodings to try
encodings = ['utf-8', 'ISO-8859-1', 'latin1', 'cp1252']

# Try reading the CSV with different encodings
df = None
for encoding in encodings:
    try:
        df = pd.read_csv('/Users/cmatthews/Desktop/Data-Analyst/Projects/Ecological-Footprint-Analysis/Resources/clean_data.csv', encoding=encoding)
        print(f"File successfully read with encoding: {encoding}")
        break
    except UnicodeDecodeError as e:
        print(f"Failed to read with encoding {encoding}: {e}")

# If no suitable encoding is found, raise an error
if df is None:
    raise ValueError("None of the specified encodings could read the file.")

# Display the first few rows of the DataFrame
print(df.head())

# Ensure required columns are present
required_columns = ['Country', 'SDGi']
for col in required_columns:
    if col not in df.columns:
        raise ValueError(f"Missing required column: {col}")

# Add Latitude and Longitude columns if they don't exist
if 'Latitude' not in df.columns or 'Longitude' not in df.columns:
    geolocator = Nominatim(user_agent="my_geocoder")
    geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)
    
    def geocode_country(country):
        try:
            location = geocode(country)
            return location.latitude, location.longitude if location else (None, None)
        except Exception as e:
            print(f"Error geocoding {country}: {e}")
            return None, None

    df['Latitude'], df['Longitude'] = zip(*df['Country'].apply(geocode_country))

# Check for missing coordinates and drop them
df = df.dropna(subset=['Latitude', 'Longitude'])

# Create a base map
m = folium.Map(location=[0, 0], zoom_start=2)

# Add data to the map
for i, row in df.iterrows():
    folium.CircleMarker(
        location=[row['Latitude'], row['Longitude']],
        radius=row['SDGi'] / 10,  # Scale the SDGi for better visualization
        popup=f"{row['Country']}: SDGi {row['SDGi']}",
        color='green' if row['SDGi'] > 70 else 'orange',
        fill=True,
        fill_color='green' if row['SDGi'] > 70 else 'orange',
        fill_opacity=0.7
    ).add_to(m)

# Save the map to an HTML file
m.save('interactive_sdgi_map.html')

print("Map has been saved as 'interactive_sdgi_map.html'.")
