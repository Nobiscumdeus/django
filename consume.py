print('Consuming an api in this application ')
import requests
response=requests.get('http://localhost:8000/love/articles')
print(response.json())