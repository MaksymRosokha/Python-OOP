def gen_primes():
    yield 2
    number = 3
    while True:
        is_prime = True
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                is_prime = False
                break
        if is_prime:
            yield number
        number += 1


if __name__ == "__main__":
    primes = iter(gen_primes())

    with open("task 4.txt", "w") as f:
        for i in range(10000):
            f.write(str(next(primes)) + "\n")