#!/usr/bin/env python3

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]
animallist = ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]

NE_list= farms[0]["agriculture"]
W_list= farms[1]["agriculture"]
SE_list= farms[2]["agriculture"]

for animals in NE_list:
    if animals in animallist:
        print(animals)
