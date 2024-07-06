# helpers.py
# Enthält diverse Hilfsfunktionen
# Alexander Winkler, winkler@zib.de
# 6. Juli 2024

# Zufallsbild von Museum-Digital laden

def randomImageUrl(instance = "berlin"):
    from random import randint
    import requests
    url = f"https://{instance}.museum-digital.de/json/objects?&s="
    res = requests.get(url)
    total = res.json()[0]["total"]
    rand_objID = randint(1, int(total))
    #get image URLs
    
    res = requests.get(f"https://{instance}.museum-digital.de/json/object/{rand_objID}")
    print(res.url)
    imgUrls = []
    for _ in res.json()["object_images"]:
        if _["filename_loc"].startswith("http"):
            iURL = _["filename_loc"]
        else:
            iURL = "https://asset.museum-digital.org/" + instance + "/" + _["folder"] + "/" + _["filename_loc"]
        imgUrls.append(iURL)
            
    return imgUrls