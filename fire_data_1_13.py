import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

infile = open("US_fires_9_1.json", "r")
outfile = open("readable_fire_data_9_1.json", "w")

fire_data = json.load(infile)

# json.dump(fire_data, outfile, indent=4)

list_of_fires = []

list_of_fires = fire_data

# print(list_of_fires[0]["latitude"])


brightness, lats, longs = [], [], []

count = 0

for fire in list_of_fires:
    bright = list_of_fires[count]["brightness"]
    lat = list_of_fires[count]["latitude"]
    long = list_of_fires[count]["longitude"]

    if list_of_fires[count]["brightness"] > 450:
        brightness.append(bright)
        lats.append(lat)
        longs.append(long)

    count += 1


data = [
    {
        "type": "scattergeo",
        "lon": longs,
        "lat": lats,
        "marker": {
            "size": 10,
            "color": brightness,
            "colorscale": "Viridis",
            "reversescale": True,
            "colorbar": {"title": "Fires"},
        },
    }
]


my_layout = Layout(title="US Fires - 9/1/2020 through 9/13/2020")

fig = {"data": data, "layout": my_layout}

offline.plot(fig, filename="US_Fires")
