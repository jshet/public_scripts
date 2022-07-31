import roundrobin 
import pytest
from collections import Counter
from itertools import combinations

test_list = ["Salah","TAA","Robertson","Jota"]

# tests for roundrobin.py

def test_sample():
    schedule_combinations = roundrobin.make_pairs(test_list)
    combos = combinations(test_list)
    assert len(combos) == len(schedule_combinations)

def test_duplicate_names():
    with pytest.raises(ValueError):
        roundrobin.make_pairs(['John', 'Jill', 'Jim', 'John'])

def test_repeated_pairings():
    pass

def test_same_person_scheduled_twice():
    pass
