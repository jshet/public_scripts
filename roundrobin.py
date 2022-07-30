people = [1, 2, 3, 4, 5, 6, 7, 8, 9]

if len(people) % 2 != 0:       # if there's not an even number of people, add a break time
    people.append("-break-")

original_person_in_position_two = people[1]   # stop when this person makes it back around

while True:
    seating = people.copy()
    pairings = []
    '''
    This is the important part. Grab the first and last elements from the list, then rotate all but the first element clockwise.
    So the first element never moves, and the remaining elements move clockwise.
    If the remaining elements go counterclockwise (as I had it previously) there are duplicates.
    '''
    while len(seating) > 0:
        pair = (seating.pop(0), seating.pop()) # get the first and last elements
        pairings.append(pair)        
    people.insert(1, people.pop())      # rotate by taking the last element from the list and insert it after the first element

    print(pairings)

    if people[1] == original_person_in_position_two:
        break
