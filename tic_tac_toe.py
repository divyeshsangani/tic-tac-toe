l = ['-','-','-','-','-','-','-','-','-']
player = computer = ""
import random
def symbol(player, computer):
    player = raw_input("select symbol X or O ")
    while player not in ('x','X','o','O'):
        print "Invalid Choice!"
        player = raw_input("select symbol O or X ")
    if player == 'x' or player == 'X':
        print "you are X"
        computer = 'o'
    else:
        print "you are O"
        computer = 'x'
    return player, computer

def draw(l):
    
    print l[0],l[1],l[2]
    print "-------------"
    print l[3],l[4],l[5]
    print "-------------"
    print l[6],l[7],l[8]


def player_first(player,computer,l):
    a=input("enter position")
    if l[a]=="-":
        l[a]=player
        draw(l)
        print
        if check_player(player,l):
            print "you win"
            print "congo!!"
        elif check_player(player,l)<>True:
            if check_tie(l):
                print "its a tie"
            else:
                b = random.randint(0,8)
                while l[b]<>"-":
                    b = random.randint(0,8)
                l[b]=computer
                draw(l)
                print
                if check_computer(computer,l):
                    print "you lose"
                elif not check_computer(computer,l):
                    if check_tie(l):
                        print "its a tie"
                    else:
                        player_first(player,computer,l)
    else:
        print"invalid entry!!"
        player_first(player.computer,l)


def check_player(player,l):
    a = [0,1,2,3,4,5,6,7,8,0,3,6,1,4,7,2,5,8,0,4,8,2,4,6]
    for i in range(0,23,3):
        if l[a[i]]==player and l[a[i+1]]==player and l[a[i+2]]==player:
            return True
    else:
        return False


def check_tie(l):
    a = 0
    for i in l:
        if i=="-":
            a+=1
    if a==0:
        return True
    else:
        return False
    
def check_computer(computer,l):
    a = [0,1,2,3,4,5,6,7,8,0,3,6,1,4,7,2,5,8,0,4,8,2,4,6]
    for i in range(0,23,3):
        if l[a[i]]==computer and l[a[i+1]]==computer and l[a[i+2]]==computer:
            return True
    else:
        return False
    
    
def computer_first(player,computer,l):
    b = random.randint(0,8)
    while l[b]<>"-":
        b = random.randint(0,8)
    l[b]=computer
    draw(l)
    print
    if check_computer(computer,l):
        print "you lose"
    else:
        if check_tie(l):
            print "its a tie"
        else:
            player_first(player,computer,l)
    
def instructions():
    print"""the instructions are as follows:
<>first you will be asked to select your team o or x
<>then after assigning teams, you will have to choose if you want to go first..
<>enter y to go first and n to go second
<>the keep entering your positions according to the table given below and win the game
<>


      0 1 2
      -----
      3 4 5
      -----
      6 7 8"""

    
instructions()
player,computer=symbol(player, computer)
a = raw_input("you wanna go first")
if a=="y" or a=="Y":
    player_first(player,computer,l)
else:
    computer_first(player,computer,l)
"press enter to exit"

            
    
                    
        











        
