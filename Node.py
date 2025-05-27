import random
class Node:
    def __init__(self,x):
        self.features = set(x)
        self.score = self.evaluate()

    def evaluate(self):
        return random.uniform(0,100) #filler

    def __str__(self):
        return f"Features: {sorted(self.features)} "
