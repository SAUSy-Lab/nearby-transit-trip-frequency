from osrm_setup import *
from nearby_stops import *
from trip_count import *
import time

start_time = time.time()

# inputs of gtfs and day to count number of trips
gtfsin = "gtfs" # unzipped folder name
dayin = "20180808"

# # downloading OSM from extensts
# dl_osm_from_extents(-79.1087,-79.6457,43.8554,43.5807)

# # setting up or killing OSRM server
# setup_osrm_local("foot")
# kill_server()


# load stops
dfp_trips = load_trips(gtfsin,dayin)
dfp_stop_times = load_stop_times(gtfsin)
print time.time() - start_time

# # running the script for a single origin
# transitstopsnearby =  stops_distance_away(gtfsin,-79.12851297,43.79407785,800)
# print transitstopsnearby
# tcd = trip_count_day(dfp_stop_times, transitstopsnearby, dfp_trips)
# print tcd

# trip_count_day(transitstopsnearby,gtfsin,dayin)

# running for a set of origins
input_data = "tor_block_pts.csv"
out_data = [["DBUID","24hr_trip_count"]]
with open(input_data,"r") as csvfile:
    reader = csv.DictReader(csvfile)
    c = 0
    for row in reader:
        c += 1
        try:
            ox = float(row["X"])
            oy = float(row["Y"])
            transitstopsnearby =  stops_distance_away(gtfsin,ox,oy,800)
            tcd = trip_count_day(dfp_stop_times, transitstopsnearby, dfp_trips)
            out_row = ([row["DBUID"],tcd])
            out_data.append(out_row)
        except:
            out_row = ([row["DBUID"],0])
            out_data.append(out_row)
        print c, "   ", time.time() - start_time
        print "------------------------------"
with open("out_data.csv", "w") as csvfile:
    writer = csv.writer(csvfile)
    for row in out_data:
        writer.writerow(row)

print time.time() - start_time
