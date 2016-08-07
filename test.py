#! /usr/bin/env python3

from Erastosthenes import Erastosthenes

erastosthenes = Erastosthenes(10000)

for prime in erastosthenes:
    print (prime, end=" ")

print()
