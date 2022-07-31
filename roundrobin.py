test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def make_pairs(people):

    '''
    Create pairs by grabbing the first and last elements from the list.
    When the round is finished, rotate all but the first player clockwise.
    The first player never moves.
    Scheduling is completed when the original person in position two makes it back to position two.
    '''

    if len(people) % 2 != 0:       # if there's not an even number of people, add a break time
        people.append("-break-")

    original_person_in_position_two = people[1]   # stop when this person makes it back around
    schedule = []
    while True:
        seating = people.copy()
        pairings = []
        while len(seating) > 0:
            pair = (seating.pop(0), seating.pop())
            pairings.append(pair)        
        people.insert(1, people.pop())
        schedule.append(pairings)
        if people[1] == original_person_in_position_two:
            break
    return schedule

if __name__ == "__main__":
    output = make_pairs(test_list)
    print(output)
