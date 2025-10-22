import random

class Coin:
    def __init__(self, denomination):
        self.denomination = denomination
        self.side = "heads"

    def throw(self):
        self.side = random.choice(["heads", "tails"])

    def __str__(self):
        return f"Coin's denomination {self.denomination} and side {self.side}"

#a
coin = Coin(1)

for i in range(15):
    coin.throw()
    print(coin)

#b
coins = [Coin(1), Coin(2), Coin(5)]
balans = 0
wins = 0
losses = 0
for i in range(100):
    balans = 0
    while balans < 20:
        for c in coins:
            c.throw()
            if c.side == "heads":
                balans += c.denomination
        if balans == 20:
            wins += 1
        elif balans > 20:
            losses += 1

print(f"Wins {wins}")
print(f"Losses {losses}")
