import requests

url = "https://sta.ci.taiwan.gov.tw/STA_Earthquake_v2/v1.0/"
response = requests.get(url)
print(response.json())
