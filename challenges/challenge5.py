#!/usr/bin/env python3
hero = input(" Which character do you want to know about? (Flash, Batman, Superman):  " )
power = input(" What statistic do you want to know about? (strength, speed, or intelligence): ")
herodict =  {"flash":{"speed": "fastest", "intelligence": "lowest", "strength": "lowest"}, "batman":{"speed": "slowest", "intelligence": "Highest", "strength": "Money"}, "superman":{"speed": "fast", "intelligence": "average", "strength": "strongest"}}
print (f'{hero}\'s {power} is: {herodict[hero][power]}' )
