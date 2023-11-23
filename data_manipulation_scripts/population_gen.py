import requests
import json
import csv

population = []

def get_city_opendata(city, country):
    tmp = 'https://public.opendatasoft.com/api/explore/v2.1/catalog/datasets/geonames-all-cities-with-a-population-500/records?refine=country:%s&refine=ascii_name:%s'
    cmd = tmp % (country, city)
    res = requests.get(cmd)
    dct = json.loads(res.content)
    out = dct['results'][0]['population']
    return out

csv_file = "finalfinal.csv"

with open(csv_file, 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[0] != "city":
            # print(row[0])
            try:
                pop = get_city_opendata(row[0], 'India')
                population.append(pop)
            except:
                print("error in", row[0])
                population.append(0)

# population = [1,2,3,4,5,6,7,8]

with open('pop.csv', 'w') as f:
    writer = csv.writer(f)
    for val in population:
        writer.writerow([val])

# Corrected some spelling and add some populations in the csv file manually