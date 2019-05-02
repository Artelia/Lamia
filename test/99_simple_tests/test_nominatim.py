import urllib2
import json

proxy = urllib2.ProxyHandler({'http': 'http://10.1.3.47:3128',
                              'https': 'http://10.1.3.47:3128'})
opener = urllib2.build_opener(proxy)
urllib2.install_opener(opener)

point=(-0.49724,44.81341)
print('start')

if True:
    request = "https://nominatim.openstreetmap.org/reverse?format=jsonv2&lat=" + str(point[1]) + "&lon=" + str(point[0])
    request += "&namedetails=1"
    print(request)
if False:        # not working
    request = "https://services.gisgraphy.com/reversegeocoding/search?format=json&lat=" + str(point[1]) + "&lng=" + str(point[0])
    print(request)
req = urllib2.Request(request, headers={'User-Agent' : "Magic Browser"})
response = urllib2.urlopen(req)



print('1')

html = response.read()
python_obj = json.loads(html)
print('ok')

print(html)
print(python_obj)
print(python_obj.keys())
print(python_obj['address'])
print(python_obj['address'])