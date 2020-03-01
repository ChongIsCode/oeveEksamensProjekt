import json
import requests
import random

headers = {
    "Accept": "application/vnd.api+json",
    "Content-Type": "application/vnd.api+json"
}

theNum = random.randrange(1,9999)
print("\nID = "+str(theNum))

response = requests.get("http://kitsu.io/api/edge/anime?filter%5Bid%5D="+str(theNum)+"&fields%5Banime%5D=canonicalTitle", headers=headers)

if response.status_code == 200:
    anime = response.json()
    info = anime.get("data")
    fuck = info[0]
    titel = fuck.get("attributes")
    print(titel.get("canonicalTitle"))

else:
    print("Failure!", response.status_code)
