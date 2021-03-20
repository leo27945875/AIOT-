import requests

url = "https://sta.ci.taiwan.gov.tw/STA_AirQuality_EPAIoT/v1.0/Things"
response = requests.get(url)
things = response.json()

datastreamURL = things['value'][0]['Datastreams@iot.navigationLink']
locationsURL = things['value'][0]['Locations@iot.navigationLink']
datastream = requests.get(datastreamURL).json()
locations = requests.get(locationsURL).json()

observationsURL = datastream['value'][0]['Observations@iot.navigationLink']
observations = requests.get(observationsURL).json()
