### a measure of nearby transit trip frequency

Computes the number of unique transit trips available within a walking distance of a point. 
Walking distance and time period can be specified as inputs.

This is only a crude measure of nearby transit availability.
It isn't a measure of transit network connectivity or access to destinations.
And shouldn't be used as an overall "transit score" of a location.

It's written in Python, uses [OSRM](http://project-osrm.org/) to build a network walking graph, and [GTFS](https://developers.google.com/transit/gtfs/) data 
to locate nearby stops and associated trips. 
It is all open source, but is partly inspired by the ESRI [BetterBusBuffers](http://transit.melindamorang.com/) and Walkscore's [TransitScore](https://www.walkscore.com/transit-score-methodology.shtml). 


#### How to use:

Setting up the network with OSM and OSRM is in **osrm_setup**

Finding bus stops with in a threshold distance is in **nearby_stops.py**

And computing number of unique trips for a list of stops is in **trip_count.py**

A sample of how to run these as a batch is in **run.py**
