# store address of API endpoint
base_url = 'https://api.exchangeratesapi.io/latest'

# make a GET request to URL
# import requests as req
# response = req.get(base_url)

# print(response.ok)
# print(response.status_code)
# print(response.text)
"""
{
  "success": false,
  "error": {
    "code": 101,
    "type": "missing_access_key",
    "info": "You have not supplied an API Access Key. [Required format: access_key=YOUR_ACCESS_KEY]"
  }
}
"""
import requests as req
import os

api_key = os.getenv('API_KEY')
if not api_key:
    raise ValueError("API key not set!")
params = {
    'access_key': api_key,
    'symbols': 'CAD, GBP' # adding here instead of ? in url is cleaner
}
# response = req.get(base_url, params=params)

import json
# print(json.dumps(response.json(), indent=4)) # much more readable
# param_url = base_url + '?symbols=CAD,GBP'
data = req.get(base_url, params=params).json()
today = data['date']
eur_to_cad = data['rates']['CAD']
print(f'Euro to Canadian Dollar as of {today} is {eur_to_cad}')



