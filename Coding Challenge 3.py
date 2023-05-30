# Coding challenge 3
#
# Richard Heiner

# Part 1
#   1. Assume you want to build two functions for discounting products on a website.
#       a. Function number 1 is for student discount which discounts the current price by 10%.
#       b. Function number 2 is for an additional discount for regular buyers which discounts an additional 5% on the
#           current student discounted price.
#       c. Depending on the situation, we want to be able to apply both discounts on the products.
#   2. Design the above two mentioned functions and apply them both simultaneously on the price.

def student_discount(price):
    x = price - (price * .1)
    return price - (price * .1)


def additional_discount(price):
    x = price - (price * .05)
    return price - (price * .05)


# Part 2
#   1. Calculate the value of mathematical expression x*(x+5)^2 where x= 5 using lambda expression.
part2 = (lambda x: x * (x + 5) ** 2)(5)

# Part 3
#   1. Consider a list in Python which includes prices of all the items in a store.
#   2. Build a function to discount the price of all the products by 10%.
#   3. Use a map to apply the function to all the elements of the list so that all the product prices are discounted.
store_items = [2.5, 10.99, 15.20, 5.66, 13.13]


def discount_items(item):
    return item - (item * .1)


# The map for part 3 is in the running part of the code.

# Part 4
#   1. Using the concept of object-oriented programming and inheritance, create a superclass named Computer, which has
#       two subclasses named Desktop and Laptop.
#   2. Define two methods in the Computer class named getspecs and displayspecs, to get the specifications and display
#       the specifications of the computer.
#           a. You can use any specifications that you want.
#   3. The Desktop class and the Laptop class should have one specification which is exclusive to them for example
#       laptop can have weight as a special specification.
#   4. Make sure that the subclasses have their own methods to get and display their special specification.
#   5. Create an object of laptop/desktop and make sure to call all the methods from the computer class as well as the
#       methods from the own class


class Computer:
    department = " "
    year = 0

    def __init__(self, department, year):
        self.department = department
        self.year = year

    def getspecs(self, department, year):
        self.department = department
        self.year = year

    def displayspecs(self):
        print("Location is " + self.department)
        print("The year of this computer is " + str(self.year))


class Desktop(Computer):
    desk_number = 0

    def __init__(self, desk_number):
        self.desk_number = desk_number

    def getdesktop(self, desk_number, department, year):
        self.getspecs(department, year)
        self.desk_number = desk_number

    def displaydesktop(self):
        self.displayspecs()
        print("The computer is at desk " + str(self.desk_number))


class Laptop(Computer):
    owner = " "

    def __init__(self, owner):
        self.owner = owner

    def getlaptop(self, owner, department, year):
        self.getspecs(department, year)
        self.owner = owner

    def displaylaptop(self):
        self.displayspecs()
        print("The owner of this laptop is " + self.owner)


# Part 5
#   1. Using the concept of operator overloading in Python, change the behavior of the multiplication operator in a way
#      that multiplication operator behaves like an addition operator.
class WeirdMath:
    def __init__(self, number):
        self.number = number

    def __mul__(self, other):
        num = self.number + other.number
        return num





# This is the main test of the code

print("Part 1\n")
cost = additional_discount(student_discount(100))
print("The total discounted cost is: $" + str(cost))

print("\nPart 2\n")
print("Calculating the fallowing expression x*(x+5)^2 where x= 5.")
print(part2)

print("\nPart 3\n")
print("Here are the original prices of the store items.")
print(store_items)
print("Here are the discounted store items.")
print(list(map(discount_items, store_items)))

print("\nPart 4\n")
laptop1 = Laptop("Richard")
desktop1 = Desktop(100)

print("Testing Laptop")
laptop1.getlaptop("Carley Randquist", "Art", 2024)
laptop1.displaylaptop()

print("\nTesting Desktop")
desktop1.getdesktop(4, "Library", 2021)
desktop1.displaydesktop()

print("\nPart 3\n We will be testing the multiplication overload. The numbers should be added together.")
one = WeirdMath(1)
two = WeirdMath(2)
three = WeirdMath(3)
four = WeirdMath(4)
print("1 x 4 should show as 5")
print(one * four)
print(four * three)


