import csv
pokenum= input(">")
with open("pokedex.txt","r") as pokedata:
    for x in csv.DictReader(pokedata):
        pokedict= dict(x)
        if pokedict["#"] == pokenum:
            print(f"""
{pokedict['Name']} #{pokedict['#']}
Type1: {pokedict['Type 1']}
Type2: {pokedict['Type 2']}

Base Stats:
HP: {pokedict['HP']}
Attack: {pokedict['Attack']}
Defense: {pokedict['Defense']}
Special Attack: {pokedict['Sp. Atk']}
Special Defence: {pokedict['Sp. Def']}
Speed: {pokedict['Speed']}""")
        elif pokenum >= "722" and pokenum <= "809":
            print(f"This pokedex does not support the Alola region")
            break
        elif pokenum >= "810" and pokenum <= "898":
            print(f"This pokedex does not support the Galar region")
            break
        else:
            print(f"ERROR! Please try again and enter a valid Pokemon number next time!")
            break
