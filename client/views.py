from django.shortcuts import render
from django.http import HttpResponse
import requests
import urllib
import json
from datetime import datetime
import time

def make24hrs(num):
    if num >= 10:
        return str(num) + ":00"
    else:
        return "0" + str(num) + ":00"

def index(request):
    return render(request, 'base.html')

def differenceCheck(current,y, bed, sleep):
    y = urllib.parse.quote(y, safe='')

    responseY = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address='+ y + "&key=AIzaSyAg3U57-8i8YWE0PEdwc05-SHzJe6-_He8")

    # Parse for Lat/Long

    respY_json_payload = responseY.json()

    # print Lat/Long in dictionaries
    y = respY_json_payload['results'][0]['geometry']['location']


    yLat = y['lat']
    yLong = y['lng']
    yTime = requests.get('https://maps.googleapis.com/maps/api/timezone/json?location='+ str(yLat) + "," + str(yLong) + "&timestamp=" + str(int(time.time())) + "&key=AIzaSyAg3U57-8i8YWE0PEdwc05-SHzJe6-_He8")
    xTime = requests.get('https://maps.googleapis.com/maps/api/timezone/json?location='+ str(current['lat']) + "," + str(current['lng']) + "&timestamp=" + str(int(time.time())) + "&key=AIzaSyAg3U57-8i8YWE0PEdwc05-SHzJe6-_He8")
    xOffset = xTime.json()['rawOffset']#offset from utc at departure
    yOffset = yTime.json()['rawOffset']#offset from utc at destination
    difference = xOffset + yOffset#difference in offset in seconds
    difference /= 1.6
    if ":" in bed:
        bed = bed.split(":")[0]
    current_bed = int(bed) * 3600 + xOffset#set standard bed time to 10 at departure
    local = int(((current_bed - difference) / 60 / 60) % 24)#works out the time you would normally go to bed but in destination time but adjusted slightly to reduce jetlag
    xGetUp = (local + int(sleep)) % 24
    remote = int((local + (xOffset + yOffset) / 3600) % 24)
    yGetUp = (remote + int(sleep)) % 24
    payload = {}
    payload['xget'] = make24hrs(xGetUp)
    payload['yget'] = make24hrs(yGetUp)
    payload['x'] = make24hrs(local)
    payload['y'] = make24hrs(remote)
    payload['xname'] = xTime.json()['timeZoneName']
    payload['yname'] = yTime.json()['timeZoneName']
    return payload
def api(request):
    if request.method == 'POST':
        diff = differenceCheck({'lat': request.POST.get('lat'), 'lng': request.POST.get('long')}, request.POST.get('destination'), request.POST.get('bed'), request.POST.get('sleep'))
    return HttpResponse(json.dumps(diff))