from urllib.request import urlopen
import json
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

import pandas as pd
df = pd.read_csv("FIPS.csv",
                   dtype={"fips": str, "Rate": float})
df = df.sort_values('Rate')
import plotly.express as px

fig = px.choropleth_mapbox(df, geojson=counties, locations='fips',
                           color=pd.cut(df["Rate"], bins=[0, 5, 10, 15, 20, 25, 30, 40, 60, 90]).astype(str),
                           color_discrete_sequence=px.colors.sequential.Plasma,
                           mapbox_style="carto-positron",
                           zoom=3, center = {"lat": 37.0902, "lon": -95.7129},
                           opacity=0.5,
                           labels={'Rate':'Murder Rate per 100,000'},
                           hover_name="County",
                           hover_data={"Rate", "State", "Deaths", "Population"},
                          )
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()
fig.write_html("fig.html")