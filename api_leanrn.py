import requests
import json

def abuse_ip(ip,age):
    url="https://api.abuseipdb.com/api/v2/check"

    headers = {
           'Accept': 'application/json',
           'Key':'4645e8877293c84741b3c96b09f7af449cc516ba19d9904fa2f5e511c2f17855edb87cebc74dbab3'
            }
    
    params={
        'ipAddress' : ip,
        'maxAgeInDays':age
    }
    responsedata=requests.get(url,headers=headers,params=params,verify=False)
    data=responsedata.json().get('data')
    if data:
        result=data.get('abuseconfidence')

        if result > 0:
            return True
        else:
            return False

abuse_ip("173.77.217.113",90)