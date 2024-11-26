# 1. Reverse Iterator
class ReverseIterator:
    def __init__(self, data):
        self.data = data
        self.index = len(data) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= 0:
            value = self.data[self.index]
            self.index -= 1
            return value
        else:
            raise StopIteration

my_list = [1, 2, 3, 4, 5]
reverse_iterator = ReverseIterator(my_list)

for num in reverse_iterator:
    print(num)

# 2. Even Iterator

class EvenIterator:
    def __init__(self, number):
        self.number = number
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.current <= self.number:
            if self.current % 2 == 0:
                value = self.current
                self.current += 1
                return value
            self.current += 1
        raise StopIteration

iterator_range = 20
even_iterator = EvenIterator(iterator_range)

for num in even_iterator:
    print(num)