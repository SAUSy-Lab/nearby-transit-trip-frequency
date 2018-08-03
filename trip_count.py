import csv
import pandas as pd

# load the trips table to a pandas dataframe, for specific service day(s)
def load_trips(gtfs,day):

    trips_table = gtfs + "/trips.txt"
    df_trips_table = pd.read_csv(trips_table)
    df_trips_table = df_trips_table[df_trips_table['service_id'].isin([1])]
    return (df_trips_table.trip_id.unique()).tolist()

# load the stop times table
def load_stop_times(gtfs):

    stop_times_table = gtfs + "/stop_times.txt"
    df_stop_times = pd.read_csv(stop_times_table)
    return df_stop_times

# counts unique trips for the input set of nearby stops
def trip_count_day(df_stop_times, bus_stop_ids, trips_list):

    df_stop_times = df_stop_times[df_stop_times['stop_id'].isin(bus_stop_ids)]
    df_stop_times = df_stop_times[df_stop_times['trip_id'].isin(trips_list)]
    unique_trips = len(df_stop_times.trip_id.unique())
    return unique_trips
