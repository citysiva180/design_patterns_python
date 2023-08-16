# Abstract class

class CarComponentFactory:
    def create_engine(self):
        pass

    def create_interior(self):
        pass

    def create_accessories(self):
        pass

# Concrete factory for Economy cars


class EconomyCarFactory(CarComponentFactory):
    def create_engine(self):
        return EconomyEngine()

    def create_interior(self):
        return EconomyInterior()

    def create_accessories(self):
        return EconomyAccessories()

# Concrete factory for Luxury cars


class LuxuryCarFactory(CarComponentFactory):
    def create_engine(self):
        return LuxuryEngine()

    def create_interior(self):
        return LuxuryInterior()

    def create_accessories(self):
        return LuxuryAccessories()

# Abstract product interfaces


class Engine:
    def start(self):
        pass


class Interior:
    def design(self):
        pass


class Accessories:
    def add_features(self):
        pass

# Concrete products for Economy cars


class EconomyEngine(Engine):
    def start(self):
        return "Starting an economy engine"


class EconomyInterior(Interior):
    def design(self):
        return "Designing an economy interior"


class EconomyAccessories(Accessories):
    def add_features(self):
        return "Adding economy accessories"

# Concrete products for Luxury cars


class LuxuryEngine(Engine):
    def start(self):
        return "Starting a luxury engine"


class LuxuryInterior(Interior):
    def design(self):
        return "Designing a luxury interior"


class LuxuryAccessories(Accessories):
    def add_features(self):
        return "Adding luxury accessories"

# Client code


def manufacture_car(factory):
    engine = factory.create_engine()
    interior = factory.create_interior()
    accessories = factory.create_accessories()
    return engine.start(), interior.design(), accessories.add_features()


# Usage
economy_car_factory = EconomyCarFactory()
luxury_car_factory = LuxuryCarFactory()

print("Economy Car:")
print(manufacture_car(economy_car_factory))

print("Luxury Car:")
print(manufacture_car(luxury_car_factory))


# In this example, we need to understand 1 thing...
# the very base class is CarComponentFactory but its hidden. Meaning, while you manufacture your luxury and economy classes are your concrete classes
# Besides these, your class for Engine, Interior and Accessories are completely scoped separately. They only add an element when in need for your class
# Now create a combo classes of this sort. Here i have added a table that makes sense

# Abstract Class    Concrete class  Parts Class  Concrete+Parts class

#  CarComponentFactory Luxury       Engine              CreateLuxuryEngine
#  CarComponentFactory Luxury       Interior            CreateLuxuryInterior
#  CarComponentFactory Luxury       Accessories         CreateLuxuryAccessories
#  CarComponentFactory Economic     Engine              CreateEconomicEngine
#  CarComponentFactory Economic     Interior            CreateEconomicInterior
#  CarComponentFactory Economic     Accessories         CreateEconomyAccessories


# now you have these options to create multiple factory scenarios in building the classes
# and some of the classes are not part of your creation.
# in this case CarComponentFactory is the most abstract function which is very well hidden
# by your code pattern


# from abc import ABC, abstractmethod


# class FoodType:
#     french = 1
#     american = 2


# class Restaurant(ABC):

#     @abstractmethod
#     def make_food(self):
#         pass

#     @abstractmethod
#     def make_drink(self):
#         pass


# class FrenchRestaurant(Restaurant):

#     def make_food(self):
#         print("Corden Bleu")

#     def make_drink(self):
#         print("Merlot")


# class AmericanRestaurant(Restaurant):

#     def make_food(self):
#         print("Ham Burgers")

#     def make_drink(self):
#         print("Coca Cola")


# class RestaurantFactory:
#     @staticmethod
#     def suggest_restaurant(r_type: FoodType):

#         if r_type == FoodType.french:
#             return FrenchRestaurant()

#         if r_type == FoodType.american:
#             return AmericanRestaurant()


# def dine_at(restaurant: Restaurant):

#     print("for dinner we are having")
#     restaurant.make_food()
#     restaurant.make_drink()


# if __name__ == "__main__":
#     suggestion_1 = RestaurantFactory.suggest_restaurant(FoodType.french)
#     suggestion_2 = RestaurantFactory.suggest_restaurant(FoodType.american)

#     dine_at(suggestion_1)
#     dine_at(suggestion_2)

# Abstract factory interface
