#!/usr/bin/env python3

class Dog:
    # Class body goes here

    # Instance method definition
    def bark(self):
        print("Woof!")
    
    def sit(self):
        print("The dog is sitting.")


fido = Dog()
snoopy = Dog()

# access instance's __dir__() method with dot notation
fido.__dir__()

# call bark() on instances
fido.bark()
snoopy.bark()


# call sit() on instances
fido.sit()
snoopy.sit()
