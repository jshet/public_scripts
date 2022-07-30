people = [1, 2, 3, 4, 5, 6, 7, 8]
n_people = len(people)
rounds = n_people - 1
n_pairs = int(n_people / 2)

all_pairs = []

while rounds > 0:
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
    all_pairs.append(pairings)          # add the list of pairs to the list of all pairs
    people.insert(1, people.pop())      # rotate by taking the last element from the list and insert it after the first element

    '''
    Another way to do the iterations would be by checking the second element in the list. 
    Stop the loop when it gets back around to the second position.
    '''
    rounds -= 1
    print(pairings)

print(all_pairs)



