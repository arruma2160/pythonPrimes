#! /usr/bin/env python3
from abc import ABCMeta, abstractmethod
import timeit

class Primes(metaclass = ABCMeta):
    """
        Definition of a base class for calculation of prime numbers
        Attributes:
            primes      (list):     list of primes up till a limit
            limit       (int):      calculate primes up till this parameter
            time_exec   (float):    time of execution/calculation of primes up till limit
        Methods:
            - __init__
            - __iter__
            - __algorithm_primes (Abstract method)
            - execution_time 
    """

    def __init__ (self, limit):
        """
            :arg    limit ( int ): calculate primes till 'limit' with limit included
        """
        self.primes = [1]
        self.limit = limit
        self.time_exec = 0.0

        start           = timeit.default_timer()
        self.primes     = self.primes + self.__algorithm_primes (  )
        self.time_exec  = timeit.default_timer() - start

    @abstractmethod
    def __iter__ ( self ):
        """
            Yields the list of primes
        """
        yield None

    @abstractmethod
    def __algorithm_primes (self):
        """
            Private method that needs to be implemented in the subclasses.
            Carries out the calculation of the primes' list 
            :arg        limit (int) : calculate primes till 'limit' with limit included
            :returns    primes(list): list of primes calculated up till limit
        """
        pass
    def execution_time (self):
        """
            Getter for time of execution
        """
        return self.time_exec
