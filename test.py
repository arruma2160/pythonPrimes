#! /usr/bin/env python3

from Erastosthenes import Erastosthenes

erastosthenes = Erastosthenes(10000)

for prime in erastosthenes:
    print (prime, end=" ")

print()

print ("erastosthenes.time_exec = " + str( erastosthenes.execution_time()) )
