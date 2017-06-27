from osrm_setup import *
from nearby_stops import *
from trip_count import *
import time

start_time = time.time()

# inputs of gtfs and day to count number of trips
gtfsin = "gtfs" # unzipped folder name
dayin = "20170322"

# # setting up or killing OSRM server
# setup_osrm_local("foot")
# kill_server()

# # running the script for a single origin
# transitstopsnearby =  stops_distance_away(gtfsin,-79.11551,43.81914,800)
# print trip_count_day(transitstopsnearby,gtfsin,dayin)

# running for a set of origins
input_data = "geocoded.csv"
out_data = [["ID","24hr_trip_count"]]
with open(input_data,"r") as csvfile:
    reader = csv.DictReader(csvfile)
    c = 0
    for row in reader:
        c += 1
        try:
            ox = float(row["X"])
            oy = float(row["Y"])
            transitstopsnearby =  stops_distance_away(gtfsin,ox,oy,800)
            tcd = trip_count_day(transitstopsnearby,gtfsin,dayin)
            out_row = ([row["ID"],tcd])
            out_data.append(out_row)
        except:
            out_row = ([row["ID"],0])
            out_data.append(out_row)
        print c
        print "--------------"
with open("t_GO_person.csv", "w") as csvfile:
    writer = csv.writer(csvfile)
    for row in out_data:
        writer.writerow(row)

print time.time() - start_time

# nearby-transit-trip-frequency
