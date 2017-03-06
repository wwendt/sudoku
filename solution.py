

assignments = []

before_naked_twins_1 = {'I6': '4', 'H9': '3', 'I2': '6', 'E8': '1',
                        'H3': '5', 'H7': '8', 'I7': '1', 'I4': '8',
                        'H5': '6', 'F9': '7', 'G7': '6', 'G6': '3',
                        'G5': '2', 'E1': '8', 'G3': '1', 'G2': '8',
                        'G1': '7', 'I1': '23', 'C8': '5', 'I3': '23',
                        'E5': '347', 'I5': '5', 'C9': '1', 'G9': '5',
                        'G8': '4', 'A1': '1', 'A3': '4', 'A2': '237',
                        'A5': '9', 'A4': '2357', 'A7': '27',
                        'A6': '257', 'C3': '8', 'C2': '237', 'C1': '23',
                        'E6': '579', 'C7': '9', 'C6': '6',
                        'C5': '37', 'C4': '4', 'I9': '9', 'D8': '8',
                        'I8': '7', 'E4': '6', 'D9': '6', 'H8': '2',
                        'F6': '125', 'A9': '8', 'G4': '9', 'A8': '6',
                        'E7': '345', 'E3': '379', 'F1': '6',
                        'F2': '4', 'F3': '23', 'F4': '1235', 'F5': '8',
                        'E2': '37', 'F7': '35', 'F8': '9',
                        'D2': '1', 'H1': '4', 'H6': '17', 'H2': '9',
                        'H4': '17', 'D3': '2379', 'B4': '27',
                        'B5': '1', 'B6': '8', 'B7': '27', 'E9': '2',
                        'B1': '9', 'B2': '5', 'B3': '6', 'D6': '279',
                        'D7': '34', 'D4': '237', 'D5': '347', 'B8': '3',
                        'B9': '4', 'D1': '5'}

rows = 'ABCDEFGHI'
cols = '123456789'

digits = '123456789'

def cross(A, B):
    return [s+t for s in A for t in B]

boxes = cross(rows, cols)

diag1 = [a[0]+a[1] for a in zip(rows, cols)]
diag2 = [a[0]+a[1] for a in zip(rows, cols[::-1])]

#nakedTwins = [box for box in values.keys() if len(values[box]) == 2]

row_units = [cross(r, cols) for r in rows]
column_units = [cross(rows, c) for c in cols]
square_units = [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]
unitlist = row_units + column_units + square_units
units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)

before_naked_twins_1 = {'I6': '4', 'H9': '3', 'I2': '6', 'E8': '1',
                        'H3': '5', 'H7': '8', 'I7': '1', 'I4': '8',
                        'H5': '6', 'F9': '7', 'G7': '6', 'G6': '3',
                        'G5': '2', 'E1': '8', 'G3': '1', 'G2': '8',
                        'G1': '7', 'I1': '23', 'C8': '5', 'I3': '23',
                        'E5': '347', 'I5': '5', 'C9': '1', 'G9': '5',
                        'G8': '4', 'A1': '1', 'A3': '4', 'A2': '237',
                        'A5': '9', 'A4': '2357', 'A7': '27',
                        'A6': '257', 'C3': '8', 'C2': '237', 'C1': '23',
                        'E6': '579', 'C7': '9', 'C6': '6',
                        'C5': '37', 'C4': '4', 'I9': '9', 'D8': '8',
                        'I8': '7', 'E4': '6', 'D9': '6', 'H8': '2',
                        'F6': '125', 'A9': '8', 'G4': '9', 'A8': '6',
                        'E7': '345', 'E3': '379', 'F1': '6',
                        'F2': '4', 'F3': '23', 'F4': '1235', 'F5': '8',
                        'E2': '37', 'F7': '35', 'F8': '9',
                        'D2': '1', 'H1': '4', 'H6': '17', 'H2': '9',
                        'H4': '17', 'D3': '2379', 'B4': '27',
                        'B5': '1', 'B6': '8', 'B7': '27', 'E9': '2',
                        'B1': '9', 'B2': '5', 'B3': '6', 'D6': '279',
                        'D7': '34', 'D4': '237', 'D5': '347', 'B8': '3',
                        'B9': '4', 'D1': '5'}



def assign_value(values, box, value):
    """
    Please use this function to update your values dictionary!
    Assigns a value to a given box. If it updates the board record it.
    """
    values[box] = value
    if len(value) == 1:
        assignments.append(values.copy())
    return values



def naked_twins(values):
    """
    #assigns to variable naked twins the box in values key if the length of that box is two
    nakedTwins = [box for box in values.keys() if len(values[box]) == 2]

    for box in nakedTwins:
        digits = values[box]
        #a, b = digit.split()
        for unit in unitlist:
            for digit in digits:    
                values[box] = values[box].replace(digit, '')
    return values    
    """
    #for box in all of the values
    for box in values:
        #if the length of a value in a box is 2
        if len(values[box]) == 2:
            #for a unit in a list of units
            for unit in unitlist:
                #for all the peers of this box
                for peer in peers[box]:
                    #if the value of the peers is equal to the value of the box
                    if values[peer] == values[box]:
                        #assign the value of the peer to the variable digits
                        digits = values[peer]
                        #for another peer of this box
                        for diff_peer in peers[box]:
                            #if the length of the values of the other peer is greater than one
                            #and the other peer doesn't equal the original peer
                            if (len(values[diff_peer]) > 1) and (diff_peer != peer):
                                #the first value of the other peer are replaced
                                values[diff_peer] = values[diff_peer].replace(digits[0],'')
                                
                                #the second value of the other peer are replaced
                                values[diff_peer] = values[diff_peer].replace(digits[1], '')
                                
    return values
    
def grid_values(grid):
    """
    Convert grid into a dict of {square: char} with '123456789' for empties.
    Args:
        grid(string) - A grid in string form.
    Returns:
        A grid in dictionary form
            Keys: The boxes, e.g., 'A1'
            Values: The value in each box, e.g., '8'. If the box has no value, then the value will be '123456789'.
    """
    chars = []
    digits = '123456789'
    for c in grid:
        if c in digits:
            chars.append(c)
        if c == '.':
            chars.append(digits)
    assert len(chars) == 81
    return dict(zip(boxes, chars))

def display(values):
    """
    Display the values as a 2-D grid.
    Args:
        values(dict): The sudoku in dictionary form
    """
    width = 1+max(len(values[s]) for s in boxes)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print(''.join(values[r+c].center(width)+('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF': print(line)
    return
    

def eliminate(values):
    solved_values = [box for box in values.keys() if len(values[box]) == 1]
    for box in solved_values:
        digit = values[box]
        
        for peer in peers[box]:
            values[peer] = values[peer].replace(digit,'')
    return values

def only_choice(values):
    for unit in unitlist:
        for digit in '123456789':
            dplaces = [box for box in unit if digit in values[box]]
            if len(dplaces) == 1:
                values[dplaces[0]] = digit
    return values

#only_choice('A1')
   

def reduce_puzzle(values):
    solved_values = [box for box in values.keys() if len(values[box]) == 1]
    stalled = False
    while not stalled:
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])
        values = eliminate(values)
        values = only_choice(values)
        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
        stalled = solved_values_before == solved_values_after
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False
    return values

def search(values):
    values = reduce_puzzle(values)
    if values is False:
        return False ## Failed earlier
    if all(len(values[s]) == 1 for s in boxes): 
        return values ## Solved!
    # Choose one of the unfilled squares with the fewest possibilities
    n,s = min((len(values[s]), s) for s in boxes if len(values[s]) > 1)
    # Now use recurrence to solve each one of the resulting sudokus, and 
    for value in values[s]:
        new_sudoku = values.copy()
        new_sudoku[s] = value
        attempt = search(new_sudoku)
        if attempt:
            return attempt

#def naked_twins(values):

     #This is my search function that will identify naked twins
    #values = search(values)
    #if all(len(values[s]) == 1 for s in boxes):
     #   return values
   # if all(len(values[s]) == 1 for s in boxes):
    #    return values
        #solved
    
    
    #this is my eliminate function, where I try to eliminate all of the naked twins...
    """
    for unit in unitlist:
        for digit in '123456789':

    nakedTwins = [box for box in values.keys() if len(values[box]) == 2]
    for box in nakedTwins:
        digit = values[box]
        for peer in peers[box]:
            values[peer] = values[peer].replace(digit,'')
    return values

    """
    """Eliminate values using the naked twins strategy.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        the values dictionary with the naked twins eliminated from peers.
    """

    # Find all instances of naked twins
    # Eliminate the naked twins as possibilities for their peers
    #twins = [box for box in values.keys() if values[box] == values[box]]
    #for box in twins:

   

    #This is my elimination function, that will eliminate naked twins from its peers
"""
    for unit in unitlist:
        for digits in '123456789'
        dplaces1 = [box for box in unit if digit in values[box]]
        dplaces2 = [box for box in unit if digit in values[box]]
        if dplaces1 == dplaces2:
            values[dplaces[0,1]] = digits
    return values

    pass
"""



def solve(grid):
    """
    Find the solution to a Sudoku grid.
    Args:
        grid(string): a string representing a sudoku grid.
            Example: '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    Returns:
        The dictionary representation of the final sudoku grid. False if no solution exists.
    """

    reduce_puzzle(grid)
    only_choice(grid)
    eliminate(grid)
    naked_twins(grid)

if __name__ == '__main__':
   # diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    #display(solve(diag_sudoku_grid))

    try:
        from visualize import visualize_assignments
        visualize_assignments(assignments)

    except SystemExit:
        pass
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')
