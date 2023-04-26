# rock paper scissor game using random module
import random
x=["Paper","Rocks","scissors"]
while True:
    Ucount=0
    Ccount=0
    Uc=int(input('''
lets start the game:
1 yes
2 No 
    '''))
    if Uc==1:
        for a in range(1,6):
            Uinput=int(input('''
1 Rock
2 paper
3 Scissors
 '''))
        if Uinput==1:
              Uchoice="Rock"
        elif Uinput==2:
              Uchoice="Paper"
        elif Uinput==3:
              Uchoice="Scissors"
        Cchoice=random.choice(x)
        if Uchoice== Cchoice:
               print("computer choice:", Cchoice)
               print("user choice:", Uchoice) 
               print("Game tie")
               Ucount=Ucount+1
               Ccount=Ccount+1
        elif(Uchoice=="Paper" and Cchoice=="Rocks" ) or (Uchoice=="Rock" and 
              Cchoice=="scissors") or (Uchoice=="Scissors" and Cchoice=="Paper"):
                print("computer choice:", Cchoice)
                print("user choice:", Uchoice) 
                print("You win")
                Ucount=Ucount+1
        else:
                print("computer choice:", Cchoice)
                print("user choice:", Uchoice) 
                print("Computer win")
                Ccount=Ccount+1

        if Ucount==Ccount:
             print("final game draw.")
             print("user score",Ucount)
             print("Computer score",Ccount)
        elif Ucount>Ccount:
             print("you win the game")
             print("user score",Ucount)
             print("Computer score",Ccount)
        else:
             print("computer win the game")
             print("user score",Ucount)
             print("Computer score",Ccount)

    else:
     break;
    


   
            

        
    

    
