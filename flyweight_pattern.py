#  Imagine you're developing a video game with a large number of enemies. Each enemy has its unique appearance,
#  such as different textures, colors, and shapes, but they all share some common properties like health points
#  and behavior. Using the Flyweight Pattern, you can optimize memory usage by sharing common properties among
#  all enemies while storing unique properties separately.

class villans:
    def display(self):
        pass


class CommonVillains(villans):
    def __init__(self, name):
        self.name = name

    def display(self):
        return f"Common villans with '{self.name}' with shared properties"

# Flyweight Properties


class VillainsFactory:
    _flyweights = {}

    @staticmethod
    def get_enemy(name):
        if name not in VillainsFactory._flyweights:
            VillainsFactory._flyweights[name] = CommonVillains(name)
        return VillainsFactory._flyweights[name]


if __name__ == "__main__":
    enemies = [
        VillainsFactory.get_enemy("Rafe"),
        VillainsFactory.get_enemy("Rafe"),
        VillainsFactory.get_enemy("Rafe"),
        VillainsFactory.get_enemy("Marlow"),
        VillainsFactory.get_enemy("Marlow"),
        VillainsFactory.get_enemy("Talbot")
    ]

    for enemies in enemies:
        print(enemies.display())
