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

txt = titel.get("canonicalTitle")
#^^ gemmer en random title i en vaiabel.
x = txt.split()
#^^ tager stringen fra txt og laver det om til en liste, hvor hvert ord er en item i listen, derefter gemmer den listen i en vaiabel.
answer = input("Choose a word that will replace a random word in the title above UwU\n")
#^^ gemmer et input i en variabel, som vi skal bruge til at bytte ud med et tilfældigt ord fra anime titlen vi fik.
result = txt.replace(random.choice(x), answer)
#^^ koden tager et tilfældigt ord fra listen x, og bytter det ud med ordet "answer" og gemmer det i en vaiabel.

print(result)
#^^ printer resultatet af ordenes udbytning.
