import subprocess

# downloading osm from extents
def dl_osm_from_extents(xmax, xmin, ymax, ymin):

    url = 'http://overpass-api.de/api/map?bbox=' + str(xmin) + ',' + str(ymin) + ',' + str(xmax) + ',' + str(ymax)

    subprocess.call(["wget", url])

    temp_name = 'map?bbox=' + str(xmin) + ',' + str(ymin) + ',' + str(xmax) + ',' + str(ymax)

    # subprocess.call(["mkdir", "osrm"])

    # rename to map.osm.xml
    subprocess.call(["mv", temp_name, "osrm/map.osm.xml"])


# set this up on a local server
def setup_osrm_local(mode):

    subprocess.call(["osrm-extract",  "osrm/map.osm.xml", "-p", "osrm/profiles/" + mode + ".lua"])

    subprocess.call(["osrm-contract", "osrm/map.osrm"])

    subprocess.call(["osrm-routed", "osrm/map.osrm"])

# kill the server if need be
def kill_server():

    subprocess.call(["sudo", "fuser", "-k", "5000/tcp"])
