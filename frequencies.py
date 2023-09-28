"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    while(len(items) != 0):
        value = 0
        key = str(items[0])
        for i in items:
            if(str(i) == key):
                value += 1
        frequencies[key] = value
        for i in range(value + 1):
            items = [i for i in items if str(i) != key]
    return frequencies
