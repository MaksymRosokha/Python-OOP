def permute(items):
    if len(items) <= 1:
        yield tuple(items)
        return

    for i in range(len(items)):
        other = items[:i] + items[i + 1:]

        for j in permute(other):
            yield (items[i],) + j


def permute_unique(items):
    items = list(set(items))
    yield from permute(items)


if __name__ == "__main__":
    for p in permute([1, 2, 3]):
        print(p)
    print("-" * 75)
    for p in permute_unique([1, 1, 2]):
        print(p)
