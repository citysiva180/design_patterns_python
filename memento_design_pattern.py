from dataclasses import dataclass


@dataclass
class Memento:
    state: str


class Originator:

    def __init__(self, state):
        self.state = state

    def create_memento(self):
        return Memento(self.state)

    def restore_memento(self, memento: Memento):
        self.state = memento.state


class Caretaker:
    memento_list = []

    def save_state(self, state: Memento):
        self.memento_list.append(state)

    def restore(self, index: int):
        return self.memento_list[index]


if __name__ == "__main__":

    # In the very first step, we create an initial state 0
    # The care taker is instantiated

    originator = Originator("initial state")
    caretaker = Caretaker()

    # Now that both the classes are instantiated, we then use the create memento
    # function which actually saves the current state. Remember, create memento is creating a
    # State while the caretaker is saving the state
    # Now the state is changes to state 1 which is then saved in the memento by caretaker
    # Again state is changed to 2 which is reflecting on print statement
    # Now comes the big deal. Now the restore_memento function is used by which an index value is passed
    # this value is number 1 which basically restores the state to number 1
    # again on passing 0 we restore to the initial state which was stored.

    caretaker.save_state(originator.create_memento())
    print(f"Current state is {originator.state}")

    originator.state = "state 1"
    caretaker.save_state(originator.create_memento())
    print(f"Current state is {originator.state}")

    originator.state = "state 2"
    caretaker.save_state(originator.create_memento())
    print(f"Current state is {originator.state}")

    originator.restore_memento(caretaker.restore(1))
    print(f"Current state is {originator.state}")

    originator.restore_memento(caretaker.restore(0))
    print(f"Current state is {originator.state}")
