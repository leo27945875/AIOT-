import requests

url = "https://sta.ci.taiwan.gov.tw/STA_AirQuality_EPAIoT/v1.0/Things"
response = requests.get(url)
print(response.json())
