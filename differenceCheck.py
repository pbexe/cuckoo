# 2 airport names
# flight time
# time difference
import requests
import geonames

# x and y is location name googlemaps
differenceCheck(x,y)
String(x)
String(y)
# concatinate string with google API for Lat/Long request
responseX = requests.get(urllib.quote('https://maps.googleapis.com/maps/api/geocode/'+x, safe=' '))
responseY = requests.get(urllib.quote('https://maps.googleapis.com/maps/api/geocode/'+y, safe=' '))

# Parse for Lat/Long
respX_json_payload = responseX.json()
respY_json_payload = responseY.json()

# print Lat/Long in dictionaries
x = (respX_json_payload['results'][0]['geometry']['location'])
y = (respY_json_payload['results'][0]['geometry']['location'])

# Split Lat/Long from dictionary
xLat = x['lat'] 
xLong = x['lng']

yLat = y['lat']
yLong = y['lng']

# Get timezone

geonames_client = geonames.GeonamesClient('demo')
geonames_resultX = geonames_client.find_timezone({xlat, xlong})
geonames_resultY = geonames_client.find_timezone({ylat, ylong})

# Test prints
# print(geonames_resultX['timezoneId'])
# print(geonames_resultY['timezoneId'])

# final variables available to other functions
# xFinal = geonames_resultX['timezoneId']
# yFinal = geonames_resultY['timezoneId']

# ALT METHOD (Doesn't use geonames module)
urlX = "http://api.geonames.org/timezoneJSON?formatted=true&lat={}&lng={}&username=demo".format(xLat,xLong)
urlY = "http://api.geonames.org/timezoneJSON?formatted=true&lat={}&lng={}&username=demo".format(yLat,yLong)

rX = requests.get(urlX) ## Make a request
rY = requests.get(urlY) ## Make a request
xFinal = rX.json()['timezoneId'] ## return the timezone
YFinal = rY.json()['timezoneId'] ## return the timezone




