import random


def random_walk(start=0, p=0.5, max_steps=None, left=None, right=None):
    position = start
    steps = 0
    while True:
        if max_steps is not None and steps >= max_steps:
            break
        if left is not None and position <= left:
            break
        if right is not None and position >= right:
            break
        steps += 1

        if random.random() < p:
            position += 1
        else:
            position -= 1

        yield position


if __name__ == "__main__":
    walk1 = random_walk(start=0, p=0.5)
    for _ in range(10):
        print(next(walk1))

    print("-" * 75)

    walk2 = random_walk(start=0, p=0.7, max_steps=15, left=-5, right=10)
    for step in iter(walk2):
        print(step)
