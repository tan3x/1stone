def decision(x):
    # >>>>> YOUR CODE HERE
    N= tuple(raw_input().split(','))
    
    n0 = N[0].strip('\'')
    n1 = N[1]
    n2 = N[2].strip(' \'')
    
    if len(N) != 3:
        raise NotImplementedError("Enter a convenient tuple.")
    if n0 == 'yes':
        if ( n1 < 29.5) :
            return 'less'
        else:
            return 'more'
    else:
        if n2 == 'good':
            return 'less'
        else:
            return 'more'

x = ('yes', 31, 'good')

# assert decision(x) == 'more'
print decision(x)