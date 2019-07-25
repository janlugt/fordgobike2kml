import json
import simplekml
import urllib3

http = urllib3.PoolManager()
response = http.request('GET', 'https://gbfs.fordgobike.com/gbfs/en/station_information.json')
station_info = json.loads(response.data)['data']['stations']
response = http.request('GET', 'https://gbfs.fordgobike.com/gbfs/en/station_status.json')
station_status = json.loads(response.data)['data']['stations']

installed_style = simplekml.Style()
installed_style.iconstyle.icon.href = 'https://member.fordgobike.com/versions/1500489851/8dResources/eightdbike/images/maps/markers/in-service/marker_100.png'
planned_style = simplekml.Style()
planned_style.iconstyle.icon.href = 'https://member.fordgobike.com/versions/1500489851/8dResources/eightdbike/images/maps/planned.png'

kml = simplekml.Kml(name = 'Ford GoBike locations')

for info in station_info:
  status = [x for x in station_status if x['station_id'] == info['station_id']][0]
  pnt = kml.newpoint(name='<![CDATA[%s]]>' % info['name'])
  pnt.coords = [(info['lon'], info['lat'])]

  if status['is_installed']:
    pnt.style = installed_style
  else:
    pnt.style = planned_style

kml.save('fordgobike.kml')
