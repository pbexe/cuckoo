# 2 airport names
# flight time
# time difference
import requests

# x and y is location name googlemaps
differenceCheck(x,y):
	String(x)
	String(y)

	responseX = requests.get(urllib.quote('https://maps.googleapis.com/maps/api/geocode/'+x, safe=' '))
	responseY = requests.get(urllib.quote('https://maps.googleapis.com/maps/api/geocode/'+y, safe=' '))

	respX_json_payload = responseX.json()
	respY_json_payload = responseY.json()

	x(respX_json_payload['results'][0]['geometry']['location'])
	x(respY_json_payload['results'][0]['geometry']['location'])