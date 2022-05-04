import pytest
from code_challenges.stack_queue_animal_shelter import AnimalShelter, Dog, Cat


def test_single_cat():
    shelter = AnimalShelter()
    cat = Cat()
    shelter.enqueue(cat)
    actual = shelter.dequeue("cat")
    expected = cat
    assert actual == expected


def test_single_dog():
    shelter = AnimalShelter()
    dog = Dog()
    shelter.enqueue(dog)
    actual = shelter.dequeue("dog")
    expected = dog
    assert actual == expected


def test_dog_preferred_but_cat_in_front():
    shelter = AnimalShelter()
    cat = Cat()
    dog = Dog()
    shelter.enqueue(cat)
    shelter.enqueue(dog)
    actual = shelter.dequeue("dog")
    expected = dog
    assert actual == expected


def test_dog_then_cat():
    shelter = AnimalShelter()
    cat = Cat()
    dog = Dog()
    shelter.enqueue(dog)
    shelter.enqueue(cat)
    shelter.dequeue("dog")
    actual = shelter.dequeue("cat")
    expected = cat
    assert actual == expected


def test_bad_pref():
    shelter = AnimalShelter()
    cat = Cat()
    dog = Dog()
    shelter.enqueue(dog)
    shelter.enqueue(cat)
    shelter.dequeue("dog")
    actual = shelter.dequeue("lizard")
    expected = None
    assert expected == actual


def test_no_pref_dequeue():
    shelter = AnimalShelter()
    cat_1 = Cat('Meowser')
    cat_2 = Cat('Fiskars')
    cat_3 = Cat('Nekosan')
    dog_1 = Dog('Woofer')
    dog_2 = Dog('Spot')
    dog_3 = Dog('Garfield')
    shelter.enqueue(dog_1)
    shelter.enqueue(cat_1)
    shelter.enqueue(cat_2)
    shelter.enqueue(dog_2)
    shelter.enqueue(dog_3)
    shelter.enqueue(cat_3)
    actual_1 = shelter.dequeue()
    actual_2 = shelter.dequeue()
    expected = [dog_1, cat_1]
    assert expected == [actual_1, actual_2]
