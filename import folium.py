import folium
import pandas as pd

# Load the new dataset
file_path = '/mnt/data/clean_data.csv'
df = pd.read_csv(file_path)

# Initialize the folium map centered around the coordinates of the new data
m = folium.Map(location=[20, 0], zoom_start=2)

# Add data to the map
for i, row in df.iterrows():
    if not pd.isna(row['Latitude']) and not pd.isna(row['Longitude']):
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
map_file_path = 'file:///Users/cmatthews/Desktop/Data-Analyst/Projects/Ecological-Footprint-Analysis/interactive_sdgi_map.html'
m.save(map_file_path)

# Read the folium map HTML content
with open(map_file_path, 'r') as map_file:
    map_html_content = map_file.read()

# Load the existing HTML file
html_file_path = 'http://127.0.0.1:5500/webpage.html'
with open(html_file_path, 'r') as html_file:
    html_content = html_file.read()

# Insert the folium map HTML content into the existing HTML structure
combined_html_content = html_content.replace('<!-- Insert map here -->', map_html_content)

# Save the combined HTML content to a new file
combined_html_file_path = 'http://127.0.0.1:5500/%3C!DOCTYPE%20html%3E.html'
with open(combined_html_file_path, 'w') as combined_html_file:
    combined_html_file.write(combined_html_content)

combined_html_file_path
