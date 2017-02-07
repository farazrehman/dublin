# Script to download APOD from NASA
  
import json
from urllib2 import Request, urlopen, URLError
  
  
request = Request('https://api.nasa.gov/planetary/apod?date=1976-01-18&api_key=7QpO8hxp3AWPiIINAFANNEDTnwb9bgqD1IW8w8Fd')
   
try:

	response = urlopen(request)
	apod_data = response.read()
	apod_data = json.load(response)
	print kittens[559:1000]
	hdURL = apod_data['hdurl']
	raw = urlopen(hdURL)
	tempfile = open('hdfile.jpg', 'wb')
	tempfile.write(raw.read())
	tempfile.close()
  
except URLError, e:
	print "No kittez. Got an eorror"
 
# This line just added

