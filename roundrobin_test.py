import roundrobin 
import pytest
from collections import Counter
from itertools import combinations

test_list = ["Salah","TAA","Robertson","Jota","VVD", "Nunez"]

# tests for roundrobin.py

def test_count_of_combinations():
    '''Does the total number of combinations match the total number of pairings?'''
    schedule = roundrobin.make_pairs(test_list)
    schedule_combos = []
    for r in schedule:
        for p in r:
            schedule_combos.append(p)
    combos = list(combinations(test_list, 2))
    assert len(combos) == len(schedule_combos)

def test_duplicate_names():
    '''Does passing a duplicate name cause an error?'''
    with pytest.raises(ValueError):
        roundrobin.make_pairs(['John', 'Jill', 'Jim', 'John'])

def test_repeated_pairings():
    '''Are any of the pairings repeated?'''
    schedule = roundrobin.make_pairs(test_list)
    pairings = []
    for round in schedule:
        for pairing in round:
            pairings.append(pairing)
    c = Counter(pairings)
    for pair in c:
        assert c[pair] == 1

def test_same_person_scheduled_twice():
    '''Is anyone schedule in multiple pairings for a single round?'''
    schedule = roundrobin.make_pairs(test_list)
    for round in schedule:
        people_in_round = []
        for pairing in round:
            for person in pairing:
                people_in_round.append(person)
        c = Counter(people_in_round)
        for person in c:
            assert c[person] == 1
