
def get_number():
    i = 1
    while True:
        yield i
        i += 1

def get_power():
    for n in get_number():
        yield n**2

def select(n, generator):
    result = list()
    iterat = iter(generator)
    try:
        for _ in range(n):
            result.append(next(iterat))
    except StopIteration:
        pass
    return result

def generate_pythagorean_triplet():
    for c in