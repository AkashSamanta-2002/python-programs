import random
def choose() : 
    words = ['COMPUTER','SCIENCE','MATHEMATICS','FOREST','INSTAGRAM','PROGRAMMING','BAGNAN','PHYSICS','UNIVERSITY','SHYAMPUR','BEYBLADE','MANKUR','TIKIAPARA','QUANTUM','TUTORIAL','SPYDER','VSCODE','CONSOLE','SETTINGS','FLIPKART','AMAZONE','PENICILINE','FREEFIRE','MIRROR','AKASH','BERLINE','ROME','FACEBOOK']
    pick = random.choice(words)
    return pick
def jumble(word) :
    jumble = ''.join(random.sample(word,len(word)))
    return jumble
def score(p1n,p2n,p1p,p2p) :
    print(p1n,'score is : ',p1p,'\n',p2n,'score is : ',p2p)
def greet(p1n,p2n,p1p,p2p) :
    if(p1p>p2p) :
        print(p1n,' is the winner.Your score is : ',p1p,'\n',p2n,'better luck next time.Your score is : ',p2p)
    else :
        print(p2n,' is the winner.Your score is : ',p2p,'\n',p1n,'better luck next time.Your score is : ',p1p)
def game() :
    p1n = input('Enter player 1 name : ')
    p2n = input('Enter player 2 name : ')
    p1p = 0
    p2p = 0
    turn = 0
    while(1) :
        if(turn%2==0) :
            picked_word = choose()
            qns = jumble(picked_word)
            print('The jumble word for',p1n,' is : ',qns)
            ans = input('Enter your answer : ')
            if(ans==picked_word) :
                p1p += 1 
                print(p1n,'you are absolutely right.The correct word is : ',picked_word)
                score(p1n,p2n,p1p,p2p)
            else :
                print(p1n,'Better luck next time.The correct word is : ',picked_word)
                score(p1n,p2n,p1p,p2p)
        else :
            picked_word = choose()
            qns = jumble(picked_word)
            print('The jumble word for',p2n,' is : ',qns)
            ans = input('Enter your answer : ')
            if(ans==picked_word) :
                p2p += 1 
                print(p2n,'you are absolutely right.The correct word is : ',picked_word)
                score(p1n,p2n,p1p,p2p)
            else :
                print(p2n,'Better luck next time.The correct word is : ',picked_word)
                score(p1n,p2n,p1p,p2p)
        play = int(input('If you want to continue enter 1 if you not,enter 0 : '))
        if(play==0) :
            break
        else :
            turn += 1
    greet(p1n,p2n,p1p,p2p)            
game()