#send data 
import urllib.request
def sendmessage(msg):
	msg = msg.replace(' ', "%20")
	msg = msg.replace('\n', "%0A")
	b=urllib.request.urlopen('https://api.thingspeak.com/update?api_key=****&field1='+msg)
	print("\nYour message has successfully been sent!")
	return
 #receive data 
 

import csv
import urllib.request
import os
def getMessage():

	url = 'https://thingspeak.com/channels/****/field/1.csv'
	urllib.request.urlretrieve(url, '<path>/1.csv')
	with open('<path>/1.csv') as csv_file:
		csv_reader = csv.reader(csv_file)
		for row in csv_reader:
			msg=row[2]
	#os.remove('<path>/1.csv')
	print("\nThe Message sent was: \n\n"+str(msg))
	return
#getMessage()


