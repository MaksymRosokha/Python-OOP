class FibonacciSequence:
    def __init__(self):
        self.f0 = 0
        self.f1 = 1

    def __iter__(self):
        yield self.f0
        yield self.f1

        while True:
            f2 = self.f0 + self.f1
            self.f0 = self.f1
            self.f1 = f2
            yield f2

import sys

if __name__ == "__main__":
    sys.set_int_max_str_digits(21000)
    fs = iter(FibonacciSequence())
    with open("task 3.txt", "w") as f:
        for i in range(100020):
            current = next(fs)
            if 100000 <= i <= 100020:
                f.write(str(current) + "\n")
            if i == 100000:
                print("F(100000) length is:", len(str(current)))