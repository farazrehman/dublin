# Script to download APOD from NASA
# Testing git chagnes
  
import json
from urllib2 import Request, urlopen, URLError
  
API_KEY =  "7QpO8hxp3AWPiIINAFANNEDTnwb9bgqD1IW8w8Fd"
APOD_BASE_URL = "https://api.nasa.gov/planetary/apod"
IMG_DATE = "2016-01-15"

APOD_URL = APOD_BASE_URL+"?date="+IMG_DATE+"&api_key="+API_KEY

print "URL: "+APOD_URL



request = Request('https://api.nasa.gov/planetary/apod?date=1976-01-18&api_key=7QpO8hxp3AWPiIINAFANNEDTnwb9bgqD1IW8w8Fd')
   
try:
	print "Read to open URL"
	response = urlopen(request)
	print response
	apod_data = response.read()
	#apod_data = json.load(response)
	#print kittens[559:1000]
	print apod_data
	hdURL = apod_data['hdurl']
	print "HDURL: "+hdURL
	raw = urlopen(hdURL)
	tempfile = open('hdfile.jpg', 'wb')
	tempfile.write(raw.read())
	tempfile.close()
  
except URLError, e:
	print "No kittez. Got an eorror"
 
# This line just added

