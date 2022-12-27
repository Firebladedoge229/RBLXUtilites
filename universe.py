import requests
input = input("Enter PlaceId: ")
URL = "https://apis.roblox.com/universes/v1/places/{}/universe".format(input)
r = requests.get(url = URL,)
data = r.json()

print("UniverseId: {}".format(data["universeId"]))