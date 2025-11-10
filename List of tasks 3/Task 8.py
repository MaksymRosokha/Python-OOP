def collatz(n):
    n = int(n)
    if n < 1:
        raise ValueError("n must be greater than 0")
    if n == 1:
        yield n
        return

    yield n
    if n % 2 == 0:
        yield from collatz(n / 2)
    else:
        yield from collatz(3 * n + 1)


class CollatzSequence:
    def __init__(self, n):
        n = int(n)
        if n < 1:
            raise ValueError("n must be greater than 0")
        self.current = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration

        if self.current == 1:
            self.current = None
            return 1

        temp = self.current
        if self.current % 2 == 0:
            self.current /= 2
        else:
            self.current = 3 * self.current + 1

        return temp

def stopping_time(n):
    """Step amount without first number"""
    return len(list(CollatzSequence(n))) - 1

def max_value(n):
    return max(list(CollatzSequence(n)))


if __name__ == "__main__":
    print("collatz(12):", list(collatz(12)))
    print("CollatzSequence(12):", list(CollatzSequence(12)))
    print("stopping_time(12):", stopping_time(12))
    print("max_value(12):", max_value(12))

    max_stopping_time = stopping_time(1)
    max_stopping_time_index = 1
    for i in range(2,101):
        next_stopping_time = stopping_time(i)
        if max_stopping_time < next_stopping_time:
            max_stopping_time_index = i
            max_stopping_time = next_stopping_time

    print(f"Max stopping time is {max_stopping_time} for {max_stopping_time_index}")