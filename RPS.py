import random
youstr="r"
scorec =0
scoreu=0
print("*** ROCK PAPER & SCISSORS GAME ***")
print("Choose \n r-ROCK \n p-PAPER \n s-SCISSORS\n e-EXIT\n")
while(youstr!="e"):

    youstr = input("Enter your choice : ")
    computer= random.choice([-1,0,1]);
    if(youstr=="e"):
        break
    if(youstr!="r" and youstr!="p" and youstr!="s" and youstr!="e"):
        print("Enter a valid option")
        print("Choose \n r-ROCK \n p-PAPER \n s-SCISSORS\n e-EXIT\n")
        continue
    youd= {"r":-1,"p":0,"s":1,"e":2}
    revd={-1:"ROCK",0:"PAPER",1:"SCISSORS"}
    you =youd[youstr]
    your=revd[you]
    print(f"computer choose: {revd[computer]}")
    print(f"you choose: {your}")
    if (computer==youd[youstr]):
        print("ITS A DRAW!!!")
    else:
        if(computer==-1 and you == 0):
            print("YOU got a point!")
            scoreu +=1
            print(f"SCORES: \n you: {scoreu} computer: {scorec}")
        elif(computer==-1 and you == 1):
            print("computer got a point!")
            scorec +=1
            print(f"SCORES: \n you: {scoreu} computer: {scorec}")
        elif(computer==0 and you == -1):
            print("Computer got a point!")
            scorec +=1
            print(f"SCORES: \n you: {scoreu} computer: {scorec}")
        elif(computer==0 and you ==1):
            print("YOU got point!!!")
            scoreu +=1
            print(f"SCORES: \n you: {scoreu} computer: {scorec}")
        elif(computer==1 and you ==0):
            print("Computer got a point!")
            scorec +=1
            print(f"SCORES: \n you: {scoreu} computer: {scorec}")
        elif(computer==1 and you ==-1):
            print("YOU got a point!!!")
            scoreu +=1
            print(f"SCORES: \n you: {scoreu} computer: {scorec}")

if(scoreu !=0 and scorec !=0):
    if(scoreu>scorec):
     print(f"*** YOU WON THE GAME WITH {scoreu-scorec} points***")
    elif(scorec>scoreu):
        print(f"*** YOU LOST THE GAME WITH {scorec-scoreu} points***")
    else:
        print("Nobody won the match!")
print("game exited succesfully!!!")