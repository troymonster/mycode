#!/usr/bin/env python3
"""Author: Troy Moore | Learning About Functions"""

import crayons

def color1():
    """This is the first color function"""
    # print 'red string' in red
    print(crayons.red('red string'))

    # Red White and Blue text
    print('{} white {}'.format(crayons.red('red'), crayons.blue('blue')))

    crayons.disable() # disables the crayons package
    print('{} white {}'.format(crayons.red('red'), crayons.blue('blue')))

    crayons.DISABLE_COLOR = False # enable the crayons package

    # This line will print in color because color is enabled
    print('{} white {}'.format(crayons.red('red'), crayons.blue('blue')))

    # print 'red string' in red
    print(crayons.red('red string', bold=True))

def color2():
    """This is the second color function"""
    # print 'yellow string' in yellow
    print(crayons.yellow('yellow string', bold=True))

    # print 'magenta string' in magenta
    print(crayons.magenta('magenta string', bold=True))

    # print 'white string' in white
    print(crayons.white('white string', bold=True))
def troyshout():
    """This is me SHOUTING AT GOD"""
    print(crayons.magenta("Troy!", bold=True))

def main():
    troyshout()
    color2()
    color1()

if __name__ == "__main__":
    main()
