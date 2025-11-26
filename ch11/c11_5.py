"""c11_5.py"""

# pylint: disable=too-few-public-methods


class Animal:
    """animal class"""

    def eat(self):
        """animal eats"""
        print("It eats.")

    def sleep(self):
        """animal sleeps"""
        print("It sleeps.")


class Bird(Animal):
    """bird class"""

    def fly(self):
        """bird files"""
        print("It flies.")


print(issubclass(Bird, Animal))

swallow = Bird()
print(isinstance(swallow, Bird))

swallow.eat()
swallow.sleep()
swallow.fly()
