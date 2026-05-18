import folium
import pandas as pd

m = folium.Map(location=[48.8566, 2.3522], zoom_start=13)

df = pd.read_csv("lieux.csv")

for index, row in df.iterrows():
    folium.Marker(
        location=[row["latitude"], row["longitude"]],
        popup=row["description"],
        tooltip=row["nom"],
        icon=folium.Icon(color="red", icon="star"),
    ).add_to(m)

m.save("map.html")
