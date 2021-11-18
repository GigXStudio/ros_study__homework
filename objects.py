class Ingredient:
    def __init__(self, name, weight, cost):
        self.weight = weight
        self.cost = cost
        self.name = name

    def get_name(self):
        return self.name

    def get_weight(self):
        return self.weight

    def get_cost(self):
        return self.cost
