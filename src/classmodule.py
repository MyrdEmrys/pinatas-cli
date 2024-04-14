import numpy as np


class Pinatas:
    def __init__(self) -> None:
        self._candies = None

    @property
    def candies(self):
        return self._candies
    
    @candies.setter
    def candies(self, value):
        self._candies = self.candies_values_processing(value)
    
    def candies_values_processing(self, value) -> list:
        if value.__len__() == 0:
            raise ValueError('not founds arguments')
        
        try:
            value = list(map(int, value))
        except:
            raise ValueError('arguments have non numeric values')
        
        for num in value:
            if num < 1:
                raise ValueError('pinata coudn`t have [candies <= 0]')
        
        return value

    def edges_multiply_value(self) -> int:
        return np.prod(self._candies[:2]) + np.prod(self._candies[-2:])

    def get_max_amount(self) -> int:
        if self._candies.__len__() == 1:
            return self._candies[0]
        
        summary = self.edges_multiply_value()

        for i in range(1, len(self._candies) - 1):
            summary += np.prod(self._candies[i-1:i+2])
        
        return int(summary)
