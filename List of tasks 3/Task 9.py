import random
import math

def estimate_pi(seed=None, batch=1):
    if batch < 1:
        raise ValueError("batch must be greater that 0")

    rnd = random.Random(seed)
    inside = 0
    total = 0

    while True:
        for _ in range(batch):
            x = rnd.uniform(-1, 1)
            y = rnd.uniform(-1, 1)

            if x ** 2 + y ** 2 <= 1:
                inside += 1
            total += 1

        pi_hat = 4 * inside / total
        yield (pi_hat, total)


def run_until_pi(eps, seed=None, batch=1000):
    pi_hat = estimate_pi(seed=seed, batch=batch)
    while True:
        next_pi_hat = next(pi_hat)
        if abs(next_pi_hat[0] - math.pi) < eps:
            return next_pi_hat


if __name__ == "__main__":
    gen = estimate_pi(seed=123, batch=1000)
    for _ in range(5):
        print(next(gen))
    print("-" * 75)

    eps = 0.0001
    pi_hat, total = run_until_pi(eps=eps, seed=123, batch=1000)
    print(f"pi_hat: {pi_hat}, eps: {eps}, total: {total}")
