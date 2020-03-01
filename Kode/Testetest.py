import json
import requests

headers = {
    "Accept": "application/vnd.api+json",
    "Content-Type": "application/vnd.api+json"
}

print("\n\n")

response = requests.get("http://kitsu.io/api/edge/anime?filter%5Bid%5D=11001&fields%5Banime%5D=canonicalTitle", headers=headers) 

if response.status_code == 200:
    print("meme")
else:
    print("Failure!", response.status_code)


anime = response.json()
# info = anime.get("data")
# fuck = info[0]





