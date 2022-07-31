test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def make_pairs(people):

    '''
    Create pairs by grabbing the first and last elements from the list.
    When the round is finished, rotate all but the first player clockwise.
    The first player never moves.
    Scheduling is completed when the original person in position two makes it back to position two.
    '''

    # Check for duplicates in people list
    if len(people) != len(set(people)):
        raise ValueError('People list cannot contain duplicate elements')

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
    import sys
    try:
        user_input = sys.argv[1]
    except:
        user_input = ""
    if user_input in ["", "--help", "-h"]:
        print(f'\n\n{"="*20}  ROUND ROBIN SCHEDULER  {"="*20}\n')
        print('''Creates a round robin schedule for pairs of two.\nEveryone meets everyone.\nTo use, pass names as arguments.\nIf an odd number of names are given, a break will be added.\n''')
        print(f'{"-"*3} EXAMPLE {"-"*3}\n')
        print('''$ python roundrobin.py "Bob" "Jose" "Sally" "Jasmine" "Dave" "Priya"\n''')
        print('''[('Bob', 'Priya'), ('Jose', 'Dave'), ('Sally', 'Jasmine')]\n[('Bob', 'Dave'), ('Priya', 'Jasmine'), ('Jose', 'Sally')]\n[('Bob', 'Jasmine'), ('Dave', 'Sally'), ('Priya', 'Jose')]\n[('Bob', 'Sally'), ('Jasmine', 'Jose'), ('Dave', 'Priya')]\n[('Bob', 'Jose'), ('Sally', 'Priya'), ('Jasmine', 'Dave')]''')
    else:
        people_list = sys.argv[1:]
        output = make_pairs(people_list)
        for r in output:
            print(r)
