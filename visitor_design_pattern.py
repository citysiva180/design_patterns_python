# Visitor
class CarComponentVisitor:
    def visit_engine(self, engine):
        pass

    def visit_wheel(self, wheel):
        pass

# ConcreteVisitor


class CarComponentStatusChecker(CarComponentVisitor):
    def visit_engine(self, engine):
        print(f"Checking status of Engine: {engine.status}")

    def visit_wheel(self, wheel):
        print(f"Checking status of Wheel: {wheel.status}")

# ConcreteVisitor


class CarComponentUpgrader(CarComponentVisitor):
    def visit_engine(self, engine):
        print(f"Upgrading Engine: {engine.model}")
        engine.status = "Upgraded"

    def visit_wheel(self, wheel):
        print(f"Upgrading Wheel: {wheel.position}")
        wheel.status = "Upgraded"

# Element


class CarComponent:
    def accept(self, visitor):
        pass

# ConcreteElement


class Engine(CarComponent):
    def __init__(self, model, status="Functional"):
        self.model = model
        self.status = status

    def accept(self, visitor):
        visitor.visit_engine(self)

# ConcreteElement


class Wheel(CarComponent):
    def __init__(self, position, status="Inflated"):
        self.position = position
        self.status = status

    def accept(self, visitor):
        visitor.visit_wheel(self)

# ObjectStructure


class Car:
    def __init__(self):
        self.components = []

    def add_component(self, component):
        self.components.append(component)

    def accept_visitor(self, visitor):
        for component in self.components:
            component.accept(visitor)


# Client code
if __name__ == "__main__":
    engine1 = Engine(model="V6")
    engine2 = Engine(model="V8")
    wheel1 = Wheel(position="Front Left")
    wheel2 = Wheel(position="Front Right")

    car = Car()
    car.add_component(engine1)
    car.add_component(engine2)
    car.add_component(wheel1)
    car.add_component(wheel2)

    status_checker = CarComponentStatusChecker()
    upgrader = CarComponentUpgrader()

    print("Checking status of car components:")
    car.accept_visitor(status_checker)

    print("\nUpgrading car components:")
    car.accept_visitor(upgrader)

    print("\nChecking status after upgrades:")
    car.accept_visitor(status_checker)
