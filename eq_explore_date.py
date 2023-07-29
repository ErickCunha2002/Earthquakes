import json
from pathlib import Path
import plotly.express as px

with open('eq_data/eq_data_30_day_m1.geojson', 'r', encoding='utf-8') as file:
    contents = file.read()
    all_eq_data = json.loads(contents)

    path = Path('eq_data/eq_data_30_day_m1.geojson')
    reable_contents = json.dumps(all_eq_data, indent=4)
    path.write_text(reable_contents)
    
all_eq_dicts = all_eq_data['features']

mags = [eq_dict['properties']['mag'] for eq_dict in all_eq_dicts]
lons = [eq_dict['geometry']['coordinates'][0] for eq_dict in all_eq_dicts]
lats = [eq_dict['geometry']['coordinates'][1] for eq_dict in all_eq_dicts]
eq_titles = [eq_dict['properties']['title'] for eq_dict in all_eq_dicts]


title = 'Global Earthquakes'
fig = px.scatter_geo(lat=lats, lon=lons, size=mags, title=title, color=mags,
    color_continuous_scale='Viridis',
    labels={'color': 'Magnitude'},
    projection='natural earth',
    hover_name=eq_titles
)


fig.show()