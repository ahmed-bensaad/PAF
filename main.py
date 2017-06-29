import os
import requests
from requests.auth import HTTPBasicAuth
import Download as dn
import json
from demo_filters import date_range_filter
from demo_filters import geo_json_geometry

# our demo filter that filters by geometry, date and cloud cover
from demo_filters import redding_reservoir
os.environ["PLANET_API_KEY"]="ae618a9b4c4448d4a1fbd71851ce835b"
# Search API request object
search_endpoint_request = {
  "item_types": ["REOrthoTile"],
  "filter": redding_reservoir
}

#Automatic input of dates
#date_debut= input("")
#if (date_debut!=""):
try:
    datewriter= open("date.txt",'r')
    List_date=datewriter.readlines()
    List_date[0]=List_date[0].replace("\n",'')
    List_date[1]=List_date[1].replace("\n",'')
    date_range_filter["config"]["gte"]=List_date[0]

#date_fin= input("")
#if (date_fin!=""):
    date_range_filter["config"]["lte"]=List_date[1]
except:
    print("Erreur dans les dates")
##Automatic input of coordinates
#L=[]
#print("debut saisie coordonnees")
#for i in range(4):
#    print("x "+str(i+1))
#    x=float(input(''))
#    print("y"+str(i+1))
#    y=float(input(''))
#    L.append([x,y])
#
#L.append(L[0])

Zone_lists=[[[
              -117.46444702148436,
              34.118626335469514
            ],
            [
              -117.16781616210936,
              34.118626335469514
            ],
            [
              -117.16781616210936,
              34.31735262740534
            ],
            [
              -117.46444702148436,
              34.31735262740534
            ],
            [
              -117.46444702148436,
              34.118626335469514
            ]],[[
              -117.20146179199217,
              32.6833081730721
            ],
            [
              -117.16232299804688,
              32.6833081730721
            ],
            [
              -117.16232299804688,
              32.722598604044066
            ],
            [
              -117.20146179199217,
              32.722598604044066
            ],
            [
              -117.20146179199217,
              32.6833081730721
            ]],[[
              -117.70683288574219,
              33.93082707134273
            ],
            [
              -117.63954162597658,
              33.93082707134273
            ],
            [
              -117.63954162597658,
              33.95759961080361
            ],
            [
              -117.70683288574219,
              33.95759961080361
            ],
            [
              -117.70683288574219,
              33.93082707134273
            ]]]

#map_nb=50
#print("saisir le nombre de la zone: entre 1 et 3")
#while(map_nb<1 or map_nb>3):
#    map_nb=int(input(''))
map_nb=List_date[2]
map_nb=map_nb.replace("\n",'')
map_nb=int(map_nb)



geo_json_geometry["coordinates"]=[Zone_lists[map_nb-1]]

datewriter.close()

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
file=open('data.txt','w')
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


#if len(L)>1:
#    X=[L[0],L[-1]]
#    dn.geturls(X)
#else:
dn.geturls(L)
