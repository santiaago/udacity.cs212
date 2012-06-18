
million = 1000000

def Q(state, action, U):
    if action == 'hold':
        return U(state+1*million)
    if action == 'gamble':
        return U(state+3*million) * .5 + U(state)*.5
import math
U = math.log10
c = 1
while True:
    if Q(c,'hold',U) == Q(c,'gamble',U):
        break
    c = c + 1
    
print c