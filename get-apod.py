# Script to download APOD from NASA
  2 
  3 import json
  4 from urllib2 import Request, urlopen, URLError
  5 
  6 request = Request('https://api.nasa.gov/planetary/apod?date=1976-01-18&api_key=7QpO8hxp3AWPiIINAFANNEDTnwb9bgqD1IW8w8Fd')
  7 
  8 try:
  9         response = urlopen(request)
 10         #apod_data = response.read()
 11         apod_data = json.load(response)
 12         #print kittens[559:1000]
 13         hdURL = apod_data['hdurl']
 14 
 15         raw = urlopen(hdURL)
 16         tempfile = open('hdfile.jpg', 'wb')
 17         tempfile.write(raw.read())
 18         tempfile.close()
 19 
 20 
 21 except URLError, e:
 22         print "No kittez. Got an eorror"
 23 
 24 
