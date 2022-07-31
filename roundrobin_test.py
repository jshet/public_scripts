import roundrobin 
import pytest

test_list = ["Salah","TAA","Robertson","Jota"]

# tests for roundrobin.py

def test_sample():
    print(roundrobin.make_pairs(test_list))

def test_duplicate_names():
    with pytest.raises(ValueError):
        roundrobin.make_pairs(['John', 'Jill', 'Jim', 'John'])

def test_repeated_pairings():
    pass

def test_same_person_scheduled_twice():
    pass
