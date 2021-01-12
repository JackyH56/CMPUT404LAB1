import requests

# print(requests.__version__)

# r = requests.get('http://google.com', auth=('user', 'pass'))
# print (r.status_code)

r = requests.get('https://raw.githubusercontent.com/JackyH56/CMPUT404LAB1/main/statusCode.py')

print(r.text)