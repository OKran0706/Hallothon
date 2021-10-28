import os
from twilio.rest import Client

account_sid = '<api id>'
auth_token = '<authentication token>'
client = Client(account_sid, auth_token)

contact_list = {'daughter':"<phone1>", "son":"<phone2>", "neighbour":"<phone3>", "mentor":"<phone4>"}
def call(number, msg):
    call = client.calls.create(
                            twiml='<Response><Say>'+msg+'</Say></Response>',
                            to=number ,
                from_= '<twilio number>'
                        )

def sms(number, msg):
	client = Client(account_sid, auth_token)
	client.messages.create(from_= '<twilio number>',
                       	to= number,
                       	body= msg)

def communicate(ip, who):

	if (ip.lower() == 'call'):
		call(contact_list[who], 'Dear '+ who + 'Call me back ')

	elif (ip.lower() == 'sms'):
		sms(contact_list[who], "Call me back "+ who)

#communicate('call', 'son')

                           