#Standard python script structure
from __future__ import print_function

import sys

#this is an error handling. good practice to have to tell people you need certain stuffs to run the script. sys.exit tells the script to STOP there. 
if not len(sys.argv) == 3:
    print ("Invalid number of arguments. Run as: python  pythonscriptname.py MTA_API_KEY BUS_LINE")
    sys.exit()

#end of standard python script structure
#start of import other things you need in this script
import os
import json

try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib
    
#setting the parameters so that users have to input these when they run my script
MTA_KEY=sys.argv[1]
BUS_LINE=sys.argv[2]

#defining the url 
url1="http://bustime.mta.info/api/siri/vehicle-monitoring.json?key="
url2="&VehicleMonitoringDetailLevel=calls&LineRef="

url=url1+MTA_KEY+url2+BUS_LINE
print (url)

#This apparently asks the system to run the whole thing as a url and download the json accordingly
response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

#writing the code that gives the output that this script is supposed to give
print ("Bus line : B52")
print ("Number of active buses: " + str(len(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])))

for i in range(len(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])):
    print ("Bus " + str(i) + " is at latitude " + str(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']) + " and longtitude " + str(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']))