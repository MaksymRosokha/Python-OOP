
def get_elements(sequence):
    try:
        iter(sequence)
    except TypeError:
        yield sequence
    else:
        for i in range(len(sequence)):
            if not isinstance(sequence[i], str):
                yield from get_elements(sequence[i])
            else:
                yield sequence[i]

if __name__ == "__main__":
    sequence = ([1, "kot"], 3, (4, 5, [7, 8, 9]))
    sequence2 = list()

    for e in get_elements(sequence):
        sequence2.append(e)

    print(sequence2)