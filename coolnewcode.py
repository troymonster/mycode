#!/usr/bin/env python3
import requests
import json

# connection data
troyid = 143982
destinyMembershipId= 4611686018430469204
membershipType= 1
api= "https://www.bungie.net/Platform"
HEADERS = {"X-API-Key":'80a39667e5064aeb84be6d0436eee4d3'}

# manifest data
with open("items.json","r") as yikes:
    hugejson= json.load(yikes)

# get the characterIds for all of Troy's characters
url1 =f"/Destiny2/1/Profile/{destinyMembershipId}?components=Characters"
char_data= requests.get(api + url1, headers=HEADERS).json()

characterIds= list(char_data["Response"]["characters"]["data"].keys())

# lil debug line
print(characterIds)

# the data object we'll fill up and return
inventory= {}

# send a GET request to each characterId to receive JSON of all non-equipped items
for characterId in characterIds:
    url2= f"{api}/Destiny2/{membershipType}/Profile/{destinyMembershipId}/Character/{characterId}/?components=CharacterInventories"
    resp= requests.get(url2, headers=HEADERS).json()
    #with open(f"/home/student/static/{characterId}.json", "w") as data:
        #json.dump(resp, data)

    # add a new character id key with an empty list value
    inventory.update({f"Character #{characterId}": []})

    # for this character, loop across all non-equipped items. Add to a list-value for each character.
    for item in resp["Response"]["inventory"]["data"]["items"]:
        itemID = str(item.get("itemHash"))
        if itemID:
            if hugejson.get(itemID):
                x= hugejson[itemID]["displayProperties"]["name"]
                inventory[f"Character #{characterId}"].append(x)
            else:
                pass
        else:
            pass

with open(f"/home/student/static/ok.json", "w") as data:
        json.dump(inventory, data)
