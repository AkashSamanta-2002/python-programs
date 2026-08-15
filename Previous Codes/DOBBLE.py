import string
import random
symbol = []
symbol = list(string.ascii_letters)
card1 = [0]*5
card2 = [0]*5
pos1 = random.randint(0,4)
pos2 = random.randint(0,4)
samesymbol = random.choice(symbol)
symbol.remove(samesymbol)
if(pos1==pos2) :
    card1[pos1] = samesymbol
    card2[pos1] = samesymbol
else :
    card1[pos1] = samesymbol
    card2[pos2] = samesymbol
    card1[pos2] = random.choice(symbol)
    symbol.remove(card1[pos2])
    card2[pos1] = random.choice(symbol)
    symbol.remove(card2[pos1])
i = 0
while(i<5) :
    if(i!=pos1 and i!=pos2) :
        alphabet1 = random.choice(symbol) 
        symbol.remove(alphabet1)
        alphabet2 = random.choice(symbol) 
        symbol.remove(alphabet2)
        card1[i] = alphabet1
        card2[i] = alphabet2
    i+=1
print(card1)
print(card2)
ans = input('Enter the common letter : ')
if(ans==samesymbol) :
    print('right')
else :
    print('Wrong')