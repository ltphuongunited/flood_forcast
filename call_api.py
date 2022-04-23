import requests
import json

def call_api():
    x = {
        "rainfall" : [0.066666667,0.1,0,0.033333333,0,0,0,0,0,0],
        "tide": [-0.37,-1.34,-1.825,-1.902,-1.498,-0.823,-0.175,0.433,1.153,1.449],
        "flooded": [49808.19372,50388.62414,50938.57857,51456.764,51945.0758,52405.46288,52840.08047,53251.67338,53701.17872,55593.49608]
    }
    url = "http://localhost:5000/predict"
    payload = json.dumps(x)
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json()

print(call_api())