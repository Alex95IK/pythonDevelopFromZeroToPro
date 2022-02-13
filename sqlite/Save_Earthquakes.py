import requests
import sqlite3


def save_earthquakes(data_file):
	conn = sqlite3.connect("earthquakes_db.db")
	c = conn.cursor()
	earthquake_list = data_file['features']
	c.execute("CREATE TABLE earthquakes (place TEXT, magnitude TEXT)")
	for earthquake in earthquake_list:
		insert_query = "INSERT INTO earthquakes VALUES (?,?)"
		c.execute(insert_query, (earthquake['properties']['place'], earthquake['properties']['mag']))
	conn.commit()
	conn.close()


def print_earthquakes():
	conn = sqlite3.connect("earthquakes_db.db")
	c = conn.cursor()
	c.execute("SELECT * FROM earthquakes;")
	for row in c:
		print(row)
	conn.commit()
	conn.close()


url = 'https://earthquake.usgs.gov/fdsnws/event/1/query?'


start_time = '2014-01-01'
end_time = '2019-01-02'
latitude = '51.51'
longitude = '-0.12'
max_radius_km = '2000'
min_magnitude = '4'


response = requests.get(url, headers={'Accept':'application/json'}, params={
		'format':'geojson',
		'starttime':start_time,
		'endtime':end_time,
		'latitude':latitude,
		'longitude':longitude,
		'maxradiuskm':max_radius_km,
		'minmagnitude':min_magnitude

	})

data = response.json()

save_earthquakes(data)

print_earthquakes()




# earthquake_list = data['features']
# count = 0
# for earthquake in earthquake_list:
# 	count += 1
# 	print(f"{count}. Place: {earthquake['properties']['place']}. Magnitude: {earthquake['properties']['mag']}.")


# start_time = input('Enter the start time')
# end_time = input('Enter the end time')
# latitude = input('Enter the latitude')
# longitude = input('Enter the longitude')
# max_radius_km = input('Enter the max radius in km')
# min_magnitude = input('Enter the min magnitude')
