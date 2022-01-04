#!/usr/bin/env python3
icecream= ["indentation", "spaces"]
tlgstudents= ["Aaron","Alex","Alonzo","Brandon","Chris","Francisco","James","Jonathan","Lillian","Manuel","Patrick","Robert","Ryan","Troy","Wes","Henry","Yalined"]
icecream.append(int(4))
input_studentno = int(input("Enter a number from 0-16: "))

print(tlgstudents[input_studentno] + " always uses " + str(icecream[2]) + " " + icecream[1] +" to indent", )
print("Now for a random choice!")
import random
randomstudent = random.randint(0,16)
print(tlgstudents[randomstudent] + " always uses " + str(icecream[2]) + " " + icecream[1] +" to indent", )
