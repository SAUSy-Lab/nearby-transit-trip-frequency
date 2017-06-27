import csv
from math import radians, cos, sin, asin, sqrt
import requests
import json


# formula for straight line distance
def haversine(lon1, lat1, lon2, lat2):

    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    m = 6367 * c * 1000
    return m

# returns all transit stop IDs within a walk distance from an origin point
def stops_distance_away(gtfs,origin_x,origin_y,distance):

    walk_speed = 1.3

    stops = gtfs + "/stops.txt"

    # grab locations of all stops
    stop_locations = []
    with open(stops, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:

            xs = float(row["stop_lon"])
            ys = float(row["stop_lat"])

            if haversine(origin_x,origin_y,xs,ys) < distance * 3:
                # some if for distance thresh

                stop_id = row["stop_id"]
                stop_locations.append([stop_id,xs,ys])

    # grab string of all the coordinates - for plugging into OSRM url
    coord_str = str(origin_x) + ',' + str(origin_y) + ';'
    for row in stop_locations:
        coord_str = coord_str + str(row[1]) + ',' + str(row[2]) + ';'
    coord_str = coord_str[:-1]

    # grab list of destinations IDs for URL string
    distr = ''
    di = 1
    while di <= len(stop_locations):
        distr = distr + str(di) + ';'
        di += 1
    distr = distr[:-1]

    # url for OSRM request
    url = 'http://localhost:5000/table/v1/walking/' + coord_str + '?sources=0&destinations=' + distr

    # getting the data via request and loading json into a python dict
    page = requests.get(url)
    data = json.loads(page.content)

    if len(stop_locations) != len(data['durations'][0]):
        return "at least one stop failed"

    c = 0

    out_stop_ids = []
    while c < len(stop_locations):
        duration = data['durations'][0][c]
        distance_to_stop = float(duration) * walk_speed
        stop_id = stop_locations[c][0]
        if distance_to_stop <= distance:
            out_stop_ids.append(stop_id)
        c += 1

    return out_stop_ids









##
