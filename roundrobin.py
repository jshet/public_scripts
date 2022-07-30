people_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def make_pairs(people):
    '''
    Create pairs by grabbing the first and last elements from the list.
    When the round is finished, rotate all but the first player clockwise.
    The first player never moves.
    '''

    if len(people) % 2 != 0:       # if there's not an even number of people, add a break time
        people.append("-break-")

    original_person_in_position_two = people[1]   # stop when this person makes it back around

    while True:
        seating = people.copy()
        pairings = []
        while len(seating) > 0:
            pair = (seating.pop(0), seating.pop())
            pairings.append(pair)        
        people.insert(1, people.pop())
        print(pairings)
        if people[1] == original_person_in_position_two:
            break

if __name__ == "__main__":
    make_pairs(people_list)
