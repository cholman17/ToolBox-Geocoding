""" CHRISTINA -- TOOLBOX #5
Geocoding and Web APIs Project Toolbox exercise
Find the MBTA stops closest to a given location.
Full instructions are at:
https://sites.google.com/site/sd15spring/home/project-toolbox/geocoding-and-web-apis
"""

import urllib   # urlencode function
import urllib2  # urlopen function (better than urllib version)
import json
from pprint import pprint

# Useful URLs (you need to add the appropriate parameters for your requests)
GMAPS_BASE_URL = "https://maps.googleapis.com/maps/api/geocode/json"
MBTA_BASE_URL = "http://realtime.mbta.com/developer/api/v2/stopsbylocation"
MBTA_DEMO_API_KEY = "wX9NwuHnZU2ToO7GmGR9uw"

# A little bit of scaffolding if you want to use it

def get_json(url):
    f=urllib2.urlopen(url)
    response_text = f.read()
    response_data = json.loads(response_text)
    return response_data

def get_lat_long(place_name):
    url = "https://maps.googleapis.com/maps/api/geocode/json?address=" + str(place_name)
    response_data = get_json(url)
    Lat = response_data["results"][0]["geometry"]["location"]["lat"] #Latitude
    Long = response_data["results"][0]["geometry"]["location"]["lng"] #Longitude

    coord = [Lat, Long] #coordinates
    return coord

def get_nearest_station(latitude, longitude):
    station = ""
    dist = 0.0
    url = MBTA_BASE_URL+"?api_key="+MBTA_DEMO_API_KEY+"&lat="+str(latitude)+"&lon="+str(longitude)+"&format=json"
    responses = get_json(url)
    try: #look for stops
        station = responses['stop'][0]['stop_name']
        dist = responses['stop'][0]['distance']
    except: #if no stops found
        print "+++ NONE FOUND +++"
    return (station, dist)

def find_stop_near(place_name):
    details = get_lat_long(place_name)
    station_pt = get_nearest_station(details[0],details[1])
    print station_pt[1]
    print station_pt[0]

if __name__ == '__main__':
    print "Cambridge: \n"
    find_stop_near("Cambridge")
    #0.0593766309320927, Broadway @ Ellery St
    p1 = raw_input("Place #1 (no spaces): ")
    find_stop_near(str(p1))
    p2 = raw_input("Place #2 (no spaces): ")
    find_stop_near(p2)
    #HarvardUniversity : 0.183475628495216, Massachusetts Ave @ Wendell St
    #BostonUniversity: 0.0850966200232506, Commonwealth Ave @ University Rd
    #WellesleyCollege: NONE
