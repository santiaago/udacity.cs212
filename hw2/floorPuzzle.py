#------------------
# User Instructions
#
# Hopper, Kay, Liskov, Perlis, and Ritchie live on 
# different floors of a five-floor apartment building. 
#
# Hopper does not live on the top floor. 
# Kay does not live on the bottom floor. 
# Liskov does not live on either the top or the bottom floor. 
# Perlis lives on a higher floor than does Kay. 
# Ritchie does not live on a floor adjacent to Liskov's. 
# Liskov does not live on a floor adjacent to Kay's. 
# 
# Where does everyone live?  
# 
# Write a function floor_puzzle() that returns a list of
# five floor numbers denoting the floor of Hopper, Kay, 
# Liskov, Perlis, and Ritchie.

import itertools

def floor_puzzle():
    floor = [0,1,2,3,4]
    permutations = itertools.permutations(floor)
    return next([Hopper,Kay,Liskov,Perlis,Ritchie]
                for (Hopper,Kay,Liskov,Perlis,Ritchie) in permutations
                if (Hopper != 4) and (Kay != 0) and (0<Liskov<4) and (Perlis>Kay) and (abs(Ritchie-Liskov)>1) and (abs(Liskov-Kay)>1))

print floor_puzzle()
