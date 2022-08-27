class Car:
    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed
    def start(self):
        print('Vroom!')
    def talk(self, driver):
        print(f'Hello, {driver}, I am {self.name}.')

# Define a race constructor with attributes of name and driver_limit
class Race:
    def __init__(self, name, driver_limit):
        # define attributes as instances
        self.name = name
        self.driver_limit = driver_limit
        # leave drivers instantiation an empty list
        self.drivers = []

    # added methods to Race class
    def add_driver(self, driver):
        # If the number of drivers already assigned to the race does
        # not exceed the driver_limit, it should add a driver to the
        # drivers list.
        if len(self.drivers) < self.driver.limit:
            self.drivers.append(driver)
            return True
        return False

    def get_average_ranking(self):
        rank = 0
        for driver in self.drivers:
            rank += driver.get_ranking()
        return rank/ len(self.drivers)

class Driver:
    # static attribute
    number_of_drivers = 0
    # constructor with attributes
    def __init__(self, name, age, ranking):
        self.name = name
        self.age = age
        self.ranking = ranking
        # increment the number of drivers by one each
        # time an instance of the class is instantiated
        Driver.number_of_drivers += 1

# test Car class
myCar = Car('Kitt', 180)

myOtherCar = Car('Speedy', 55)

myCar.talk('Michael')

# defines a course
course = Race('Seattle 500', 4)


# adds drivers
driver1 = Driver('Dale Earnhardt', 29, 100)
driver2 = Driver('Lewis Hamilton', 36, 83)
driver3 = Driver('Eliud Kipchoge', 36, 95)
driver4 = Driver('Sebastian Vettel', 34, 76)
driver5 = Driver('Ayrton Senna', 34, 99)

# add drivers to the course
course.add_driver(driver1)
course.add_driver(driver2)
course.add_driver(driver3)
course.add_driver(driver4)
course.add_driver(driver5)
print(course.get_average_ranking())