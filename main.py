import os
import requests
from requests.auth import HTTPBasicAuth
import Download as dn
import json

# our demo filter that filters by geometry, date and cloud cover
from demo_filters import redding_reservoir
os.environ["PLANET_API_KEY"]="ae618a9b4c4448d4a1fbd71851ce835b"
# Search API request object
search_endpoint_request = {
  "item_types": ["REOrthoTile"],
  "filter": redding_reservoir
}

result = \
  requests.post(
    'https://api.planet.com/data/v1/quick-search',
    auth=HTTPBasicAuth(os.environ['PLANET_API_KEY'], ''),
    json=search_endpoint_request)
    
   
a=json.loads(result.text)
#print a
L= [a['features'][i]['id'] for i in range(len(a['features']))]
#print L

dn.geturls(L)