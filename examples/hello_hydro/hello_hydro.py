#!/usr/bin/env python
'''
hello_hydro.py

An example module used for teaching the UW Land Surface Hydrology Group how to
use Python, Git, and Github.
'''

import letters


def main():

    # Say hello to the world
    letters.hello_world()

    # Say hello to Joe
    letters.hello_joe('Today is Monday')

    # Add your own hello function to letters.py
    # Then call that function from here...

    letters.hello_oriana('Today isn\'t necessarily Wednesday, Joe. Gosh, your '
                         'function needs to be more intelligent... ;)')

    letters.hello_diana('finally cleaning out my email inbox')

    letters.hello_yifan('I am learning git today')

    # All done, say goodbye
    letters.goodbye_world()

    return


if __name__ == '__main__':
    main()
