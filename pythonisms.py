

from decorators import calc_time_elapsed


class  CustomCollection:

    def __init__(self, size):
        self.size = size


    def __iter__(self):
        self.current = 0
        return self

    def __next__(self):

        if self.current >= self.size:
            raise StopIteration()
        
        res = self.current
        self.current += 1
        return res

    def __eq__(self, other):
        return self.size == other.size

    def __bool__(self):
        return self.size > 0


    @calc_time_elapsed
    def count_to_one_thousand(self):
        count = 0
        for _ in range(1000):
            count += 1
    
    @calc_time_elapsed
    def count_to_one_million(self):
        count = 0
        for _ in range(1000000):
            count += 1
            
    


    



    