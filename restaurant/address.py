import geocoder
import folium

map_osm = folium.Map(location=[40.35891, 49.834549], zoom_start=13)
map_osm.add_child(folium.Marker(location=[40.35891, 49.834549], popup="Neftchilar Avenue 78", 
icon=folium.Icon(color='green')))
map_osm.save('restaurant/templates/restaurant/address.html')