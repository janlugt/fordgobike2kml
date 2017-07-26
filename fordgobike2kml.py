import json
import simplekml
import urllib2

response = urllib2.urlopen('https://gbfs.fordgobike.com/gbfs/en/station_information.json')
station_info = json.loads(response.read())['data']['stations']
response = urllib2.urlopen('https://gbfs.fordgobike.com/gbfs/en/station_status.json')
station_status = json.loads(response.read())['data']['stations']

kml = simplekml.Kml(name = 'Ford GoBike locations')

for info in station_info:
  status = [x for x in station_status if x['station_id'] == info['station_id']][0]
  pnt = kml.newpoint(name='<![CDATA[%s]]>' % info['name'])
  pnt.coords = [(info['lon'], info['lat'])]

kml.save('fordgobike.kml')
