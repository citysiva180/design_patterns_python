# AbstractClass
class HouseTemplate:
    def build_house(self):
        self.build_foundation()
        self.build_walls()
        self.build_roof()
        self.decorate()

    def build_foundation(self):
        raise NotImplementedError(
            "build_foundation must be implemented by subclasses")

    def build_walls(self):
        raise NotImplementedError(
            "build_walls must be implemented by subclasses")

    def build_roof(self):
        raise NotImplementedError(
            "build_roof must be implemented by subclasses")

    def decorate(self):
        # Optional hook method for additional customization
        pass

# ConcreteClass


class WoodenHouse(HouseTemplate):
    def build_foundation(self):
        print("Building Wooden Foundation")

    def build_walls(self):
        print("Building Wooden Walls")

    def build_roof(self):
        print("Building Wooden Roof")

# ConcreteClass


class BrickHouse(HouseTemplate):
    def build_foundation(self):
        print("Building Brick Foundation")

    def build_walls(self):
        print("Building Brick Walls")

    def build_roof(self):
        print("Building Brick Roof")

    def decorate(self):
        print("Adding Brick Decorations")


# Client code
if __name__ == "__main__":
    wooden_house = WoodenHouse()
    brick_house = BrickHouse()

    print("Building Wooden House:")
    wooden_house.build_house()

    print("\nBuilding Brick House:")
    brick_house.build_house()
