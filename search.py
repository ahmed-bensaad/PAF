import os
import requests
from requests.auth import HTTPBasicAuth
import dic
import Download as dn
import urllib
# our demo filter that filters by geometry, date and cloud cover
from demo_filters import redding_reservoir
os.environ["PLANET_API_KEY"]="2f17fa8a5d774ad9bf62d6e4d14fd25d"
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
    
    
a=dic.dictionnaire(result.text)
L= [a['features'][i]['id'] for i in range(len(a['features']))]

dn.geturls(L)

    
