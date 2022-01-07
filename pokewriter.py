import csv 
while True: 
    pokenum= input("Enter a Pokemon number:\n>") 
    if pokenum.isdigit(): 
        break 
with open("pokedex.txt","r") as pokedata: 
    for x in csv.DictReader(pokedata): 
        pokedict= dict(x) 
        try: 
            if pokedict["#"] == str(pokenum): 
                pokewrite = open("dexentries.txt", "a")
                pokewrite.write(f""" 
    {pokedict['Name']} #{pokedict['#']} 
    Type1: {pokedict['Type 1']} 
    Type2: {pokedict['Type 2']} 
    Base Stats: 
    HP: {pokedict['HP']} 
    Attack: {pokedict['Attack']} 
    Defense: {pokedict['Defense']} 
    Special Attack: {pokedict['Sp. Atk']} 
    Special Defence: {pokedict['Sp. Def']} 
    Speed: {pokedict['Speed']}\n""") 
            elif pokenum >= 722 and pokenum <= 809: 
                print(f"This pokedex does not support the Alola region") 
                break 
            elif pokenum >= 810 and pokenum <= 898: 
                print(f"This pokedex does not support the Galar region") 
                break 
        except: 
              pass 
