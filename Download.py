# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 10:48:39 2017

@author: abensaad
"""
import time
import os
import requests
def geturls(L):
    item_type = "PSOrthoTile"
    asset_type = "analytic"
   # os.system("export PLANET_API_KEY=2f17fa8a5d774ad9bf62d6e4d14fd25d")
    for i in range(len(L)):
        item_id = L[i]
        print("\033[33mDébut aquisition: Photo "+str(i+1)+" sur "+str(len(L))+"\033[0m")

# setup auth
        session = requests.Session()
        session.auth = (os.environ['PLANET_API_KEY'], '')

# request an item
        item = \
        session.get(
            ("https://api.planet.com/data/v1/item-types/" +
            "{}/items/{}/assets/").format(item_type, item_id))
      # print item.text
# extract the activation url from the item for the desired asset
        item_activation_url = item.json()[asset_type]["_links"]["activate"]

        print("\033[33mDemande d'activation\033[0m")
        response = session.post(item_activation_url)
        print response
        while response.status_code==202:
            time.sleep(5)
            response = session.post(item_activation_url)



        if(response.status_code)==204:
            print("\033[32mActivation réussie!! Aquisition du lien de la photo\033[0m")
            ch=os.popen("curl -L -H "+ '"' + "Authorization: api-key $PLANET_API_KEY" + '"' +" 'https://api.planet.com/data/v1/item-types/"+item_type+"/items/"+item_id+"/assets/' \
            | jq ."+asset_type+".location ").readlines()

            print("\033[32mLien aquis! Fin aquisition photo "+str(i+1)+"\033[32m")

            print("\033[33mVérification de l'autorisation de téléchargement \033[0m")
            ch1=os.popen("curl -L -H "+ '"' + "Authorization: api-key $PLANET_API_KEY" + '"' +" 'https://api.planet.com/data/v1/item-types/"+item_type+"/items/"+item_id+"/assets/' \
            | jq ."+asset_type+"._permissions ").readlines()
            if ch1== ['[\n', '  "download"\n', ']\n']:

                print ("\033[32mAutorisation accordée\033[32m")

                print("\033[33mDébut téléchargement\033[0m")
                os.system("curl -L -o '/cal/homes/abensaad/Desktop/PAF/PAF/image"+str(i+1)+"' "+ch[0])
                print("\033[32mFin téléchargement\033[0m")
        else:

            print("\033[31mAutorisation non accordée, échec de téléchargement de la photo \033[0m"+str(i+1))
