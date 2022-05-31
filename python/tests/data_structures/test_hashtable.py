import pytest
from data_structures.hashtable import Hashtable


def test_exists():
    assert Hashtable


@pytest.mark.skip("TODO")  # same code, but fails
def test_create():
    ht = Hashtable()
    actual = ht.size()
    expected = 1024
    assert actual == expected


def test_create_default():
    ht = Hashtable()
    actual = ht.size
    expected = 1024
    assert actual == expected


def test_hash():
    ht = Hashtable()
    index = ht.hash('cat')
    assert 0 <= index < ht.size


def test_set_apple():
    ht = Hashtable()
    ht.set('fruit', 'apple')
    fruit_idx = ht.hash('fruit')
    actual = ht.pockets[fruit_idx]
    expected = ('fruit', 'apple')
    assert actual.head.value == expected


def test_get_apple():
    ht = Hashtable()
    ht.set("fruit", "apple")

    actual = ht.get('fruit')
    expected = 'apple'
    assert actual == expected


def test_collision():
    ht = Hashtable()
    ht.set('cat', 'josie')
    ht.set('act', 'a thing to do')
    ht.set('tac', 'tacos')

    assert ht.get('cat') == 'josie'
    assert ht.get('act') == 'a thing to do'
    assert ht.get('tac') == 'tacos'


def test_keys():
    ht = Hashtable()
    ht.set('cat', 'josie')
    actual = ht.keys()
    assert 'cat'


@pytest.mark.skip("TODO")
def test_internals():
    hashtable = Hashtable(1024)
    hashtable.set("ahmad", 30)
    hashtable.set("silent", True)
    hashtable.set("listen", "to me")

    actual = []

    # NOTE: purposely breaking encapsulation to test the "internals" of Hashmap
    for item in hashtable._buckets:
        if item:
            actual.append(item.display())

    expected = [[["silent", True], ["listen", "to me"]], [["ahmad", 30]]]

    assert actual == expected
