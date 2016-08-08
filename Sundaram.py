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
    """
    def __init ( self, limit ):
        super().__init__ ( limit )

    def _Primes__algorithm_primes ( self ):
        pass

    def __iter__ ( self ):
        for prime in self.primes:
            yield prime
