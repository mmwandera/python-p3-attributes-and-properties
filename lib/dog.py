#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name='A Dog named Dawg', breed='Corgi'):
        self.name = name
        self.breed = breed

    # Define a name property for your Dog class. The name must be of type str and between 1 and 25 characters.
    # If the name is invalid, the setter method should print() "Name must be string between 1 and 25 characters."
    def get_name(self):
        return self._name
    
    def set_name(self, name):
        if type(name) == str and 1 <= len(name) <= 25:
            self._name = name
        else:
            print("Name must be string between 1 and 25 characters.")

    name = property(get_name, set_name)

    
    # Define a breed property for your Dog class.
    # If the breed is invalid, the setter method should print() "Breed must be in list of approved breeds." The breed must be in the following list of dog breeds:
    def get_breed(self):
        return self._breed
    
    def set_breed(self, breed):
        if breed in APPROVED_BREEDS:
            self._breed = breed
        else:
            print("Breed must be in list of approved breeds.")

    breed = property(get_breed, set_breed)
    
