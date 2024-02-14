import plotly.express as px
import pandas as pd
import plotly.graph_objects as go

# read the data set
df = pd.read_csv('https://raw.github.khoury.northeastern.edu/acroak/5800_group_project/keegan/final_dataset.csv?token=GHSAT0AAAAAAAAANYCR2GW742FPYYVQI4UEZCP77IQ')

# create figure
fig = px.scatter_mapbox(df,
                        lon = df['long'], 
                        lat = df['lat'],
                        hover_name = df['Place'],                        
                        zoom = 6,
                        width = 1200,
                        height = 900,
                        color = df['Centroid Index'],
                        size = [.5]*len(df),
                        size_max=10,
                        title = 'Kruskals Clusters and Creeps')


fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0, "t":50, "l":0, "b":10})

fig.show()