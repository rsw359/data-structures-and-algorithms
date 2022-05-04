from data_structures.queue import Queue


class AnimalShelter:
    def __init__(self):
        self.shelter = Queue()
        self.dog = Queue()
        self.cat = Queue()

    def enqueue(self, animal):
        if animal.type == 'cat':
            self.cat.enqueue(animal)
            self.shelter.enqueue(animal)
        elif animal.type == 'dog':
            self.dog.enqueue(animal)
            self.shelter.enqueue(animal)

    def dequeue(self, pref=None):

        if pref is None:
            any_animal = self.shelter.dequeue()
            if any_animal.type == 'cat':
                self.cat.dequeue()
                return any_animal
            elif any_animal.type == 'dog':
                self.dog.dequeue()
                return any_animal

        if pref != 'cat' or pref != 'dog':
            return None

        elif pref == 'cat':
            cat = self.cat.dequeue()
            return cat

        elif pref == 'dog':
            dog = self.dog.dequeue()
            return dog


class Dog:
    def __init__(self, name=None):
        self.type = 'dog'
        self.name = name


class Cat:
    def __init__(self, name=None):
        self.type = 'cat'
        self.name = name
