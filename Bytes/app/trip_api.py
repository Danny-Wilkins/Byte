#key: c59f647c-ebaf-47f1-92d7-5302e6641e36
import requests
import json
import operator
import numpy as np
from scipy import stats
from geopy.geocoders import Nominatim

API_KEY =  "c59f647c-ebaf-47f1-92d7-5302e6641e36"

def main():
	
	values = getRestaurantsInArea(raw_input("Enter address: "))

	for i in values:
		print i[0], i[1][0], i[1][1]

	#print json.dumps(r.json(), indent=4, sort_keys=True)

def getRestaurantsInArea(address, distance=2, ratings=1):
	try:
		loc = geolocator(address)
	except:
		print "Location not found. Please try again."
		return getRestaurantsInArea(raw_input("Enter address: "))
		

	r = requests.get('https://api.tripadvisor.com/api/partner/2.0/map/{},{}/restaurants?key={}&distance={}'.format(loc['lat'], loc['lng'], API_KEY, distance))

	#print json.dumps(r.json(), indent=4, sort_keys=True)
	js = r.json()

	prices = []
	ratings = []

	for item in js['data']:
		if(item['price_level'] == None):
			continue

		prices.append(float(len(item['price_level'])))
		ratings.append(float(item['rating']))

	prices = np.array(prices)
	ratings = np.array(ratings)

	try:
		slope, intercept, r_value, p_value, std_err = stats.linregress(prices, ratings)
	except:
		print "No restaurants found nearby. Please try again."
		return getRestaurantsInArea(raw_input("Enter address: "))
		

	#print slope, intercept, r_value, p_value, std_err

	values = {}

	for item in js['data']:
		if(item['price_level'] == None):
			continue

		#print item['name'], value(item, slope, intercept)
		v = value(item, slope, intercept)

		values[item['name']] = (round(v, 3), grade(v))

	values = sorted(values.items(), key=operator.itemgetter(1), reverse=True)

	return values

def getHotelsInArea(address, distance=2):
	try:
		loc = geolocator(address)
	except:
		getHotelsInArea(raw_input("Enter address: "), raw_input("Max distance: "))
		return

	r = requests.get('https://api.tripadvisor.com/api/partner/2.0/map/{},{}/hotels?key={}&distance={}'.format(loc['lat'], loc['lng'], API_KEY, distance))

	#js = json.dumps(r.json(), indent=4, sort_keys=True)/restaurants?key={}&distance=2.0'.format(key))
	js = r.json()

	prices = []
	ratings = []

	for item in js['data']:
		if(item['price_level'] == None):
			continue

		prices.append(float(len(item['price_level'])))
		ratings.append(float(item['rating']))

	prices = np.array(prices)
	ratings = np.array(ratings)

	slope, intercept, r_value, p_value, std_err = stats.linregress(prices, ratings)
	#print slope, intercept, r_value, p_value, std_err

	values = {}

	for item in js['data']:
		if(item['price_level'] == None):
			continue

		#print item['name'], value(item, slope, intercept)

		v = value(item, slope, intercept)

		values[item['name']] = (round(v, 3), grade(v))

	values = sorted(values.items(), key=operator.itemgetter(1), reverse=True)
	
	return values


def value(item, slope, intercept):
	predicted = len(item['price_level']) * slope + intercept

	actual = float(item['rating'])

	deviation = round(actual - predicted, 3) * 100

	return deviation

def grade(value):
	if 100 > value > 66:
		return 'A'
	elif 66 >= value > 33:
		return 'B'
	elif 33 >= value > -33:
		return 'C'
	elif -33 >= value > -66:
		return 'D'
	elif -66 >= value:
		return 'F'
	else:
		return 'A'

def geolocator(address):
    geolocator = Nominatim()
    location = geolocator.geocode(address)
    print(location.address)

    #print location.latitude, location.longitude

    return {'lat':location.latitude, 'lng':location.longitude}


if __name__ == '__main__':
	main()
