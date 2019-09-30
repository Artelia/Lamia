import urllib3
import json


default_headers = urllib3.make_headers(proxy_basic_auth='myusername:mypassword')
http  = urllib3.ProxyManager( 'http://10.1.3.47:3128', headers=default_headers)


"""
opener = urllib3.build_opener(proxy)
urllib3.install_opener(opener)
"""
point=(-0.49724,44.81341)
print('start')

if False:
    request = "https://nominatim.openstreetmap.org/reverse?format=jsonv2&lat=" + str(point[1]) + "&lon=" + str(point[0])
    request += "&namedetails=1"
    print(request)
if False:        # not working
    request = "https://services.gisgraphy.com/reversegeocoding/search?format=json&lat=" + str(point[1]) + "&lng=" + str(point[0])
    print(request)
if True :
    request = "https://api-adresse.data.gouv.fr/reverse/?lon=2.37&lat=48.357&type=street"
    #request = "https://stackoverflow.com/"
    print(request)

req = http.request('GET', request)

#print(req.json())

if True:
    python_obj = json.loads(req.data)
    #print(python_obj)
    print(python_obj['features'][0]['properties']['name'])
    print(python_obj['features'][0]['properties']['label'])
    print(python_obj['features'][0]['properties']['score'])

