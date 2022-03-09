import csv
import plotly.express as px

rows = []
with open('final2.csv', 'r') as f:
    csvreader = csv.reader(f)
    for i in csvreader:
        rows.append(i)
headers = rows[0]
starRows = rows[1:]

name = []
mass = []
radius = []
distance = []
gravity = []

for star_data in starRows:
    name.append(star_data[1])
    mass.append(star_data[3])
    radius.append(star_data[4])
    distance.append(star_data[2])
    gravity.append(star_data[5])

fig1 = px.bar(x=name, y=mass, title="Star Masses")
fig1.show()
fig2 = px.bar(x=name, y=radius, title="Star Radii")
fig2.show()
fig3 = px.bar(x=name, y=distance, title="Star Distance")
fig3.show()
fig4 = px.bar(x=name, y=gravity, title="Star Gravity")
fig4.show()
