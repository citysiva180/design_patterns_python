# Component (Base interface)
class Employee:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def show_details(self):
        pass

# Leaf (Individual employee)
class IndividualEmployee(Employee):
    def show_details(self):
        print(f"{self.name} - {self.role}")

# Composite (Manager with subordinates)
class Manager(Employee):
    def __init__(self, name, role):
        super().__init__(name, role)
        self.subordinates = []

    def add_subordinate(self, subordinate):
        self.subordinates.append(subordinate)

    def remove_subordinate(self, subordinate):
        self.subordinates.remove(subordinate)

    def show_details(self):
        print(f"{self.name} - {self.role}")
        for subordinate in self.subordinates:
            subordinate.show_details()

# Client code
if __name__ == "__main__":
    ceo = Manager("John", "CEO")
    
    manager1 = Manager("Alice", "Manager")
    manager2 = Manager("Bob", "Manager")
    
    employee1 = IndividualEmployee("Eve", "Developer")
    employee2 = IndividualEmployee("Charlie", "Designer")
    
    manager1.add_subordinate(employee1)
    manager2.add_subordinate(employee2)
    
    ceo.add_subordinate(manager1)
    ceo.add_subordinate(manager2)
    
    ceo.show_details()
