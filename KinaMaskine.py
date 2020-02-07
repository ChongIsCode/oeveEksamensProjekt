import requests

api = requests.get('https://www.cardmarket.com/en/Magic')

if api.status_code == 200:
    #Hvis siden er oppe, definerer den det som text i en variabel
    t = api.text
    #Så bliver teksten printet
    print(t)
