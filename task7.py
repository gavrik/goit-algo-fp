import random


class Rolls:
    def __init__(self, roll_sum, num_rolls):
        self.roll_summ = roll_sum
        self.roll_count = 0
        self.probability = 0
        self.num_rolls = num_rolls

    def __repr__(self):
        return f"{self.roll_summ} | {self.roll_count} | {self.probability} %"

    def add_count(self):
        self.roll_count += 1
        self.change_probability()

    def change_probability(self):
        self.probability = self.roll_count * 100 / self.num_rolls


def simulate_dice_rolls(num_rolls):
    probabilities = [Rolls(i, num_rolls) for i in range(13)]
    # print(probabilities)
    for i in range(num_rolls):
        p = random.randint(1, 6) + random.randint(1, 6)
        # print(p)
        probabilities[p].add_count()

    print("Number of Rolls: ", num_rolls)
    for p in probabilities:
        if p.roll_summ in [0, 1]:
            continue
        print(p)


if __name__ == "__main__":
    for r in [10, 100, 1000, 10000, 100000, 1000000]:
        simulate_dice_rolls(r)
