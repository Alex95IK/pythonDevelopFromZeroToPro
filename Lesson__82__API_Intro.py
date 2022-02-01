import requests

url = 'https://earthquake.usgs.gov/fdsnws/event/1/query?'
response = requests.get(url,headers = {'Accept': 'application/json'}, params={
	'format':'geojson',
	'starttime':'2014-01-01',
	'endtime':'2019-01-02',
	'latitude':'51.51',
	'longitude':'-0.12',
	'maxradiuskm':'2000'
	})


data = response.json()

for x in range(len(data['features'])):
	item = (data['features'][x]['properties'])
	try:
		if item['mag'] >= 6:
			print(item.get('place') ,item.get('mag'))
			# print(i ,item.get(i))
	except:
		continue
		# print('Sorry, I\'m can\'t :(')
	

# for_iter_item = len(data['features'])
# iter_item = iter(for_iter_item)

# print(iter_item)






# print(item)









# print(len(data['features']))