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
S= [a['features'][i]['properties']['acquired']for i in range(len(a['features']))]
M= [a['features'][i]['properties']['satellite_id']for i in range(len(a['features']))]
##print a['features'][i]['properties'].keys()L
#print S
#print L
#print type(S[0])
print('Copie de donnees')
file=open('/cal/homes/abensaad/Desktop/PAF/PAF/data.txt','w')
for i in range(len(a['features'])):
    file.write("image "+str(i+1))
    file.write('\n')
for i in range(len(a['features'])):    
    file.write(str(S[i]))
    file.write('\n')
for i in range(len(a['features'])):    
    file.write(str(M[i]))
    file.write('\n')
file.close()    
print('fin copie de donnees')
X=[L[0],L[-1]]

dn.geturls(X)


