#! /usr/bin/env python3

from Erastosthenes import Erastosthenes
from Sundaram import Sundaram

erastosthenes = Erastosthenes(100000)

for prime in erastosthenes:
    print (prime, end=" ")

print()

print ("erastosthenes.time_exec = " + str( erastosthenes.execution_time()) )


print ( " ==================== " )

sundaram = Sundaram(100000)
for prime in sundaram:
    print ( prime, end = " " )

print()

print ("sundaram.time_exec = " + str( sundaram.execution_time() ) )
