## Animal is-a object ( yet,sort of confusing) look at the example
class Animal(object):
    pass

##?
class Dog(Animal):
    def _init_(self, name):
        ##?
        self.name = name
    

##?
class Cat(Animal):
    def _init_(self, name):
        ##?
        self.name = name
    
class Bird(Animal):
    def _init_(self, name):
        ##?
        self.name = name
