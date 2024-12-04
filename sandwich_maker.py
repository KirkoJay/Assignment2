
class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for ingredient, amount in ingredients.items():
            if self.machine_resources[ingredient] >= amount:
                return True
            else:
                return False

    def make_sandwich(self, sandwich_size, order_ingredients):
        for ingredient, amount in ingredients.items():
            self.machine_resources[ingredient] -= amount