from typing import Generator
# uma classe serbindo de iterator e iterable
class Count_up:
    def __init__(self, x : int):
        self.limit = x
        self.a = 0
        self.b = 1
        self.i = 1
    
    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b, self.i = self.b, self.b + self.i, self.i + 1 
        if self.a > self.limit:
            raise StopIteration
        return self.a

# Generator:

def count_up(x : int) -> Generator[int, None, None]:
    """
        Generator para sequencia
    """
    a = 0
    b = 1
    i = 1

    while b < x:
        a, b, i = b, b + i, i + 1
        yield a
    
a = count_up(70)
for i in a:
    print(i)