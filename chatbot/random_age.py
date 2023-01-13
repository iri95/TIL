import requests

r = requests.get('https://api.agify.io/?name=이상훈').json()
print(r)
print(type(r))
print(r['name'],'의 나이는',r['age'],'입니다.')