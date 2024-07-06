# helpers.py
# Enthält diverse Hilfsfunktionen
# Alexander Winkler, winkler@zib.de
# 6. Juli 2024

import requests

# Bild-URL zu einer ObjektID:
def imgFromObjID(objID, instance = "berlin"):
    imgUrls = []
    while len(imgUrls) == 0:
        try:
            res = requests.get(f"https://{instance}.museum-digital.de/json/object/{objID}")
            for _ in res.json()["object_images"]:
                if _["filename_loc"].startswith("http"):
                    iURL = _["filename_loc"]
                else:
                    iURL = "https://asset.museum-digital.org/" + instance + "/" + _["folder"] + "/" + _["filename_loc"]
            imgUrls.append(iURL)
        except Exception as e:
            print(e)
            
    return imgUrls

# Zufallsbild von Museum-Digital laden
def randomImageUrl(instance = "berlin") -> list:
    from random import randint
    url = f"https://{instance}.museum-digital.de/json/objects?&s="
    res = requests.get(url)
    total = res.json()[0]["total"]
    rand_objID = randint(1, int(total))    
    imgUrls = imgFromObjID(rand_objID, instance)
    return imgUrls

# Liste von Objekt-IDs einer Collection auf Museum-Digital
def collectionsObjects(collID, instance = "berlin", maximumRecords = None):
    res = requests.get(f"https://{instance}.museum-digital.de/json/objects?&s=collection:{collID}")
    total = int(res.json()[0]['total'])
    objectsIDs = []
    if maximumRecords is not None and maximumRecords < total:
        until = maximumRecords
    else:
        until = total
    for i in range(0,until,24):
        res = requests.get(f"https://{instance}.museum-digital.de/json/objects?&s=collection:{collID}&startwert={i}").json()
        for r in res:
            objectsIDs.append(r['objekt_id'])
    return objectsIDs
            
