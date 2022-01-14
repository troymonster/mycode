#!/usr/bin/env python3
import sys
import time

def ghost():
    ghost= """
                 _     _
                / |   | \  
               /  |   |  \   
            _ /   |___|   \__
         _/_______/ __ \______\_
        /________| |__| |_______\    
         \        \____/     __ /
          \_      ____     _/
             \   |    |   /  
              \  |    |  /   
               \_|    |_/    

    """
    print(ghost)

#0.05 delay prints faster than 0.1 delay
def print1by1fast(text, delay=0.05):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)

def print1by1slow(text, delay=0.1):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)

def greeting():
    print1by1fast(f"""
Hello Guardian! I am your Ghost.
I am here to help guide you through your various options in this Bungie API.
""")


if __name__ == "__main__":
    ghost()
