def solve_btfc( puzzle ):    
   
    # get a list of the empty squares (remaining variables)
    empty_squares = get_empty_squares( puzzle )

    # if there are no remaining empty squares we're done
    if len(empty_squares) == 0: 
        print "Woohoo, success! Check it out:"
        print_puzzle( puzzle )
        return 1
    
    square = get_random_square( empty_squares )
    row = square[0]
    col = square[1]
    
    remaining_values = get_remaining_values( puzzle )
   
    values = list( remaining_values[col+row*9] )
    
    while len( values ) != 0:        
        value = values[ int( math.floor( random.random()*len( values ) ) ) ]
        values.remove(value)        
        if forward_check( remaining_values, value, row, col ):
            puzzle[row][col] = value
            if solve_btfc( puzzle ):
                return 1
            else:
                puzzle[row][col] = 0
                
    return 0