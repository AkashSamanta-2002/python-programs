import random 
movies = ['AVENGERS','TITANIC','STAR WARS','JUNGLE BOOK']
def choice() :
    ch = random.choice(movies)
    return ch
def Question(movie) :
    L = []
    for i in range(len(movie)) :
        if(movie[i]==' ') :
            L.append(' ')
        else :
            L.append('*')
    qn = ''.join(L)
    return qn
def check(letter,movie) :
    c=movie.count(letter) 
    if(c>0) :
        return True
    else : 
        return False
def unlock(movie,letter,qn) :
    ref = list(movie)
    qn_list = list(qn)
    temp = []
    n = len(movie)
    for i in range(n) :
        if(ref[i]==' ' or ref[i]==letter) :
            temp.append(ref[i])
        else :
            if(qn_list[i]=='*') :
                temp.append('*')
            else :
                temp.append(ref[i])
    new_qn = ''.join(temp)
    return new_qn
def score(p1n,p2n,p1p,p2p) :
    print(p1n,'Your score is : ',p1p,'\n',p2n,'Your score is : ',p2p)    
def greet(p1n,p2n,p1p,p2p) :
    if(p1p>p2p) :
        print(p1n,'congrats,you won your points is : ',p1p,'\n',p2n,'better luck next time, your score is : ',p2p)
    elif(p2p>p1p) :
        print(p2n,'congrats,you won your points is : ',p2p,'\n',p1n,'better luck next time, your score is : ',p1p)
    else : 
        print('The match is draw')
            
def game() :
    p1n = input('Enter player 1 name : ')
    p2n = input('Enter player 2 name : ')
    p1p = 0
    p2p = 0
    turn = 0
    playing = True
    while playing :
        picked_movie = choice()
        qn = Question(picked_movie)
        if(turn%2==0) :
            not_answered = True
            while not_answered :
                print(p1n,'Your turn! Guess the movie : ',qn)
                d = int(input('If you want to guess the movie press 1 if you want  to guess the letter press 2 : '))
                if(d==2) :
                    letter = input('Guess the letter : ')
                    if(check(letter,picked_movie)) :
                        modified_qn = unlock(picked_movie,letter,qn)
                        print('Your guess is right heres the modified qn : ',modified_qn)
                        qn = modified_qn
                        if(modified_qn==picked_movie) :
                            print('Your Guess is right the movie is : ',picked_movie)
                            p1p+=1
                            score(p1n,p2n,p1p,p2p)
                            not_answered = False
                    else :
                        print('The letter is not there, try again')
                else :
                    ans = input('Guess the full name of ihe movie : ')
                    if(ans==picked_movie) :
                        print('Your guess is correct the movie is : ',picked_movie)
                        p1p+=1
                        score(p1n,p2n,p1p,p2p)
                        not_answered = False
                    else : 
                        print('Your guess is wrong, try again')
                        
        else :
            not_answered = True
            while not_answered :
                print(p2n,'Your turn! Guess the movie : ',qn)
                d = int(input('If you want to guess the movie press 1 if you want  to guess the letter press 2 : '))
                if(d==2) :
                    letter = input('Guess the letter : ')
                    if(check(letter,picked_movie)) :
                        modified_qn = unlock(picked_movie,letter,qn)
                        print('Your guess is right heres the modified qn : ')
                        qn = modified_qn
                        if(modified_qn==picked_movie) :
                            print('Your Guess is right the movie is : ',picked_movie)
                            p1p+=1
                            score(p1n,p2n,p1p,p2p)
                    else :
                        print('The letter is not there, try again')
                else :
                    ans = input('Guess the full name of ihe movie : ')
                    if(ans==picked_movie) :
                        print('Your guess is correct the movie is : ',picked_movie)
                        p2p+=1
                        score(p1n,p2n,p1p,p2p)
                        not_answered = False
                        playing = False
                    else : 
                        print('Your guess is wrong, try again')     
        con = int(input('If you want to continue press 1, if you not press 0 : '))
        if(con==0) :
            greet(p1n, p2n, p1p, p2p)
            playing = False 
        else :
            turn = turn + 1
game()