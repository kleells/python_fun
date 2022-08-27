class Person:
    def __init__(self,in_name,in_age):
        self.name = in_name
        self.age = in_age
    def get_name(self):
        return self.name

# create a Customer class that inherites from the Person class
class Customer(Person):
    def __init__(self, in_name, in_age):
        # add super() to access the methods and properties of
        # the parent class
        super().__init__(in_name, in_age)
        # boolean for whether the customer has a ticket
        self.hasTicket = False
        # boolean for whether the customer is currently in the zoo
        self.inZoo = False
    
    # a buy_ticket method
    def buy_ticket(self):
        # message for purchase of a child's ticket
        if self.age <= 12:
            print(f"{self.name} has one children's tickets for admission to the zoo.")
        # message for purchase of an adult ticket
        else:
            print(f"{self.name} has one adult ticket for admission to the zoo.")
        # hasTicket is changed to True
        self.hasTicket = True

    # enter_zoo method
    def enter_zoo(self, zoo):
        if self.hasTicket:
            # set hasTicket to False because the customer handed the ticket in
            # for admission
            self.hasTicket = False
            # add_customer method from Zoo class is called
            zoo.add_customer(self.name)
            # Customer's attribute, inZoo is chaged to true
            self.inZoo = True
        else:
            print("Please purchase a ticket for admission in to the zoo.")

    def exit_zoo (self, zoo):
        if self.inZoo:
            # inZoo needs to be set to False
            self.inZoo = False
            # zoo class's remove_customer method is called
            zoo.remove_customer(self.name)

class Zoo:
    def __init__(self,name="Local Zoo"):
        self.name = name
        self.animals = []
        self.customers = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"{self.name} has a(n) {animal}")

    def add_animals(self, animals):
        self.animals.extend(animals)
        print(f"{self.name} has many animals")

    def add_customer(self, name):
        self.customers.append(name)
        print(f"{name} has entered {self.name}")

    def remove_customer(self, name):
        self.customers.remove(name)
        print(f"{name} has left {self.name}")

    def visit_animals(self):
        for a in self.animals:
            print(f"visiting {a.get_name()}")
        a.make_noise()
        a.eat_food()

class Animal:
    def __init__(self,name):
        self.name = name
    def get_name(self):
        return self.name
    def make_noise(self):
        print("Every animal makes noise")
    def eat_food(self):
        print("All creatures need sustenance")

# make fish, bird and chimp subclass. make_noise and eat_food 
# should override the parent, Animal class
class Fish(Animal):
    def __init__(self, name):
        super().__init__(name)
    def make_noise(self):
        print(f"{self.name} says bubble, bubble, bubble.")
    def eat_food(self):
        print(f"{self.name} eats smaller fish, there's plenty of them.")

class Bird(Animal):
    def __init__(self, name):
        super().__init__(name)
    def make_noise(self):
        print(f"{self.name} says chirp, chirp, chirp.")
    def eat_food(self):
        print(f"{self.name} eats seeds, nuts and berries.")

class Chimp (Animal):
    def __init__(self, name):
        super().__init__(name)
    def make_noise(self):
        print(f"{self.name} says grunt and eee eee eee")
    def eat_food(self):
        print(f"{self.name} eat fruit, nuts and leaves.")

nycZoo = Zoo("NYC Zoo")

salmon = Fish("salmon")
robin = Bird("robin")
bonobo = Chimp("bonobo")
nycZoo.add_animals([salmon, robin, bonobo])

alice = Customer("Alice",25)
bob = Customer("Bob",20)
charlie = Customer("Charlie",10)
dave = Customer("Dave",30)
for c in [alice, bob, charlie, dave]:
    c.buy_ticket()
    c.enter_zoo(nycZoo)
nycZoo.visit_animals()
for c in [alice, bob, charlie, dave]:
    c.exit_zoo(nycZoo)