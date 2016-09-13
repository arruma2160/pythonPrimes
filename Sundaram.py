#! /usr/bin/env python3

from primesClass import Primes

class Sundaram ( Primes ):
    """
        Definition of a concrete class for calculation of prime numbers
        Follows the algorithm for calculation of prime numbers given by Sundara
        Attributes:
            limit       (int):      calculate primes up till this parameter
        Example of use:
            Sundaram( 100 ) -> it calculates the primes using the algorithm of Sundaram till 100
        Exposed methods:
            __iter__ ()      -> yields the prime numbers calculated (concrete method)
            execution_time() -> returns the time that it has taken to calculate the prime numbers (inherited method)
            max_prime()      -> returns the highest prime in the list (inherited method)
    """
    def __init ( self, limit ):
        super().__init__ ( limit )

    def _algorithm_primes ( self ):
        numbers = set ( range ( 2, self.limit ) )
        n = (self.limit - 2 )//2
        for i in range ( 1, n + 1 ):
            j = i
            while ( i + j + 2*i*j ) <= n :
                numbers.discard ( i + j + 2*i*j )
                j += 1
        primes = [2,3] + [ 2*x + 1 for x in numbers if 2*x + 1 < self.limit ] 
        return primes

    def __iter__ ( self ):
        for prime in self.primes:
            yield prime
