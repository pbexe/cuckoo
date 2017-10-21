from django.shortcuts import render
from django.http import HttpResponse
import requests
import urllib
import json
from datetime import datetime
import time
def index(request):
    return render(request, 'base.html')

def differenceCheck(current,y):
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
    xOffset = xTime.json()['rawOffset']
    yOffset = yTime.json()['rawOffset']
    difference = xOffset + yOffset
    return difference


def api(request):
    if request.method == 'POST':
        print(request.POST.get('destination'))
        print(request.POST.get('lat'))
        print(request.POST.get('long'))
        diff = differenceCheck({'lat': request.POST.get('lat'), 'lng': request.POST.get('long')}, request.POST.get('destination'))
    return HttpResponse(diff)