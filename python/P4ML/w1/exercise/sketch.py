# def decision(x):
N= tuple(raw_input().split(','))

if len(N) != 3:
    raise NotImplementedError("Enter a proper tuple ")

n0 = N[0].strip('\'')
n1 = N[1]
n2 = N[2].strip(' \'')
decision = 'neutral'

if n0 == 'yes':
    if ( n1 < 29.5) :
        decision = 'less'
    else:
        decision = 'more'
else:
    if n2 == 'good':
        decision = 'less'
        print n2
    else:
        decision = 'more'

print decision
# assert decision == 'more' 

# x = ('yes', 31, 'good')
# decision(x)

# x = ('yes', 31, 'good')

# assert decision(x) == 'more'


