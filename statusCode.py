import requests

r = requests.get('http://google.com', auth=('user', 'pass'))
print (r.status_code)