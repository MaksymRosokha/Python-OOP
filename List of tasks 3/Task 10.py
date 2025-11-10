import math


def estimate_e():
    n = 0
    e_hat = 0
    while True:
        e_hat += 1 / math.factorial(n)
        n += 1
        yield e_hat


def approx_e(eps):
    terms_used = 0
    hat_e = estimate_e()

    while True:
        next_hat_e = next(hat_e)
        terms_used += 1

        if abs(math.e - next_hat_e) < eps:
            return (next_hat_e, terms_used)


if __name__ == "__main__":
    gen = estimate_e()
    for _ in range(10):
        print(next(gen))
    print("-" * 75)
    
    eps = 0.0001
    e_hat, terms_used = approx_e(eps=eps)
    print(f"e_hat: {e_hat}, eps: {eps}, terms_used: {terms_used}")
