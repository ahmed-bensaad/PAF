# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 10:48:39 2017

@author: abensaad
"""

import os
import requests
def geturls(L):
    item_type = "REOrthoTile"
    asset_type = "visual"
    os.system("export PLANET_API_KEY=2f17fa8a5d774ad9bf62d6e4d14fd25d")
    for i in range(len(L)):
        item_id = L[i]
        print("Début aquisition du "+str(i+1)+"éme lien de photo satellite sur"+str(len(L)+1))

# setup auth
        session = requests.Session()
        session.auth = (os.environ['PLANET_API_KEY'], '')

# request an item
        item = \
        session.get(
            ("https://api.planet.com/data/v1/item-types/" +
            "{}/items/{}/assets/").format(item_type, item_id))

# extract the activation url from the item for the desired asset
        item_activation_url = item.json()[asset_type]["_links"]["activate"]
    
        print("Demande d'activation")
        response = session.post(item_activation_url)

        if(response.status_code)==204:
             print("Activation réussie!! Aquisition du lien de la photo")
        ch=os.popen("curl -L -H "+ '"' + "Authorization: api-key $PLANET_API_KEY" + '"' +" 'https://api.planet.com/data/v1/item-types/REOrthoTile/items/"+item_id+"/assets/' \
            | jq .visual.location ").readlines()
        
        print("Lien aquis! Fin aquisition photo "+str(i+1))
        print("Début téléchargement")
        print(ch[0])
        os.system("curl -L -o 'image"+str(i+1)+"' "+ch[0])
        print("Fin téléchargement")