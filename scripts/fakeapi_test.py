import requests

url= 'https://fakestoreapi.com/products'

response= requests.get(url= url)

if response.status_code == 200:
    data = response.json()
    print(data)

else:
    print(f"error:{response.status_code}")