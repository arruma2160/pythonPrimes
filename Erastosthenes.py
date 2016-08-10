#! /usr/bin/env python3

from primesClass import Primes

class Erastosthenes ( Primes ):
    """
        Definition of a concrete class for calculation of prime numbers
        Follows the algorithm for calculation of prime numbers given by Erastosthenes
        Attributes:
            limit       (int):      calculate primes up till this parameter
        Example of use:
            Erastosthenes( 100 ) -> it calculates the primes using the algorithm of Erastosthenes till 100
        Exposed methods:
            __iter__ ()      -> yields the prime numbers calculated (concrete method)
            execution_time() -> returns the time that it has taken to calculate the prime numbers (inherited method)
            max_prime()      -> returns the highest prime in the list (inherited method)
    """
    
    def __init__ ( self, limit ):
        super().__init__ ( limit )


    def _algorithm_primes ( self ):
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
