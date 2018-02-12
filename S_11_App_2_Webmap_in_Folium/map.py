import folium
import pandas

map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Mapbox Bright")

data = pandas.read_csv("Volcanoes.txt")

lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

fgv = folium.FeatureGroup(name="Volcanoes")
fgp = folium.FeatureGroup(name="Population")


def color(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'


for lt, ln, elev in zip(lat, lon, elev):
    fgv.add_child(
        folium.CircleMarker(location=[lt, ln], radius=6, popup=str(elev) + " m", fill_color=color(elev),
                            fill_opacity=0.7,
                            color='grey', fill=True))

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
                            style_function=lambda x: {
                                'fillColor': 'green' if x['properties']['POP2005'] < 10000000
                                else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000
                                else 'red'}))


map.add_child(fgp)
map.add_child(fgv)
map.add_child(folium.LayerControl())

map.save("Map1.html")
