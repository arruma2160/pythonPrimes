#! /usr/bin/env python3

from primesClass import Primes

class Erastosthenes ( Primes ):
    
    def __init__ ( self, limit ):
        super().__init__ ( limit )


    def _Primes__algorithm_primes ( self ):
        numbers = set (range(2,self.limit))
        result  = []
        while ( True ):
            try:
                num = numbers.pop()
                result.append(num)
                i = 2
                dis = i*num
                while dis <= self.limit:
                    numbers.discard ( dis )
                    i += 1
                    dis = i*num
            except KeyError:
                break
        return result

    def __iter__ ( self ):
        for prime in self.primes:
            yield prime
