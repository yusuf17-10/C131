import csv
import plotly.express as px
rows = []
with open("C131.csv","r")as f:
    csvReader = csv.reader(f)
    for row in csvReader:
        rows.append(row)
headers = rows[0]
headers[0] = "row_number"
planet_data_row = rows[1:]

solar_system_planet_count = {}

for planet_data in planet_data_row:
    if solar_system_planet_count.get(planet_data[11]):
        solar_system_planet_count[planet_data[11]]+=1
    else:
        solar_system_planet_count[planet_data[11]]=1
max_planet_solar = max(solar_system_planet_count,key = solar_system_planet_count.get)

print(f"{max_planet_solar} : {solar_system_planet_count[max_planet_solar]}") 

temp_planet_data = list(planet_data_row)
for planet_data in temp_planet_data:
    planet_mass = planet_data[3]
    if planet_mass.lower() == "unknown":
        planet_data_row.remove(planet_data)
        continue
    else:
        planet_mass_value  = planet_mass.split(" ")[0]
        planet_mass_ref  = planet_mass.split(" ")[1]
        if planet_mass_ref == "Jupiters":
            planet_mass_value = float(planet_mass_value)* 317.8
        planet_data[3]=planet_mass_value

    planet_radius = planet_data[7]

    if planet_radius.lower() == "unknown":
        planet_data_row.remove(planet_data)
        continue
    else:
        planet_radius_value  = planet_radius.split(" ")[0]
        planet_radius_ref  = planet_radius.split(" ")[2]
        if planet_radius_ref == "Jupiter":
            planet_radius_value = float(planet_radius_value)* 317.8
        planet_data[7]=planet_radius_value

koi_planets = []
for planet_data in planet_data_row:
    if max_planet_solar == planet_data[11]:
        koi_planets.append(planet_data)
print(koi_planets)

koi_planets_masses = []
koi_planets_names = []

for planet_data in koi_planets:
    koi_planets_masses.append(planet_data[3])
    koi_planets_names.append(planet_data[1])

koi_planets_masses.append(1)
koi_planets_names.append("Earth")

fig = px.bar(x = koi_planets_names,y=koi_planets_masses)
fig.show()


temp_planet_rows = list(planet_data_row)
for planet_data in temp_planet_rows:
    if planet_data[1].lower() == "koi-351":
        planet_data_row.remove(planet_data)
    
planet_masses = []
planet_names = []
planet_radius = []

for planet_data in planet_data_row:
    planet_masses.append(planet_data[3])
    planet_names.append(planet_data[1])
    planet_radius.append(planet_data[7])

planet_gravity = []
for index,name in enumerate(planet_names):
    gravity = (float(planet_masses[index])*5.972e+24) / (float(planet_radiuses[index])*float(planet_radiuses[index])*6371000*6371000) * 6.674e-11 
    planet_gravity.append(gravity)
