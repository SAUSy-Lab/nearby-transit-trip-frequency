import csv

# function for counting the number of unique trips for a select set of bus stops in a
# inputs a list of bus IDs, name of gtfs folder, and the date in question
def trip_count_day(bus_stop_ids, gtfs, day):

    trips_table = gtfs + "/trips.txt"
    stop_times_table = gtfs + "/stop_times.txt"
    calender_dates = gtfs + "/calendar_dates.txt"

    # get list of all service_ids on specified date
    service_ids_day = []
    with open(calender_dates) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row["date"] == day:
                service_ids_day.append(row["service_id"])

    #
    unique_trips = []
    with open(stop_times_table, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['stop_id'] in bus_stop_ids:
                if row['trip_id'] not in unique_trips:
                    unique_trips.append(row['trip_id'])


    # loop over trips, and see if unique_trip id and service_id_day match

    out_trips = []
    with open(trips_table, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row["trip_id"] in unique_trips:
                if row["service_id"] in service_ids_day:
                    out_trips.append(row["trip_id"])


    return len(out_trips)
