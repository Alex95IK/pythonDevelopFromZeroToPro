import requests

starttime = input('Enter the start time: ')
endtime = input('Enter the end time: ')
latitude = input('Enter the latitude: ')
longitude = input('Enter the longitude: ')
maxradiuskm = input('Enter the max radius in km: ')
minmagnitude = input('Enter the min magnitude: ')

url = 'https://earthquake.usgs.gov/fdsnws/event/1/query?'
response = requests.get(url, headers={'Accept': 'application/json'}, params={
	'starttime': starttime,
	'endtime': endtime,
	'latitude': latitude,
	'longitude': longitude,
	'maxradiuskm': maxradiuskm,
	'minmagnitude': minmagnitude
	})

data = response.json()


features_list = data['features']
num = 0

for item in features_list:
	num += 1
	print(f"{num}. Place: {item['properties']['place']}. Magnitude: {item['properties']['mag']}.")








		# 'starttime':'2014-01-01',
		# 'endtime':'2019-01-02',
		# 'latitude':'51.51',
		# 'longitude':'-0.12',
		# 'maxradiuskm':'2000'
