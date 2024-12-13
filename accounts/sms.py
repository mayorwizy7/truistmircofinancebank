from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
import requests


account_sid = 'AC409d2a53ebd19c7b4989b4efff52acc7'
auth_token = '526fe9078c864698c2337433581b160d'
client = Client(account_sid, auth_token)



def sms(receiver, message1):
    user_number = str(receiver)
    url = "https://api.ng.termii.com/api/sms/send"
    
    payload = {
            "to": user_number,
            "from": "ATBank",
            "sms": message1,
            "type": "plain",
            "channel": "generic",
            "api_key": "TLSUG3Mrs8lJwtzYz1JAXslZw6bzSrdGsYFlXbhgufSYrVQxWExnxdHbZ2yF0k",
        }
    headers = {
    'Content-Type': 'application/json',
    }
    response = requests.request("POST", url, headers=headers, json=payload)
    print(response.text)