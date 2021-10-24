#send data 
import csv
import urllib.request
import os
def getMessage():

	url = 'https://thingspeak.com/channels/1545354/field/1.csv'
	urllib.request.urlretrieve(url, '/Users/chiragr/Desktop/1.csv')
	with open('/Users/chiragr/Desktop/1.csv') as csv_file:
		csv_reader = csv.reader(csv_file)
		for row in csv_reader:
			msg=row[2]

	return str(msg)

