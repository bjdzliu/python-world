class SquaresIterable1:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.limit:
            result = self.current ** 2
            self.current += 1
            return result
        else:
            raise StopIteration

# Example usage:
squares_iterable = SquaresIterable1(5)

# Using a for loop to iterate over the custom iterable
# for square in squares_iterable:
#     print(square)


aa=iter(squares_iterable)
for a in aa:
    print(a)
