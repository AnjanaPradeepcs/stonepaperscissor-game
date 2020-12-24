import random
cchoice=["Stone","paper","scissor"]
while True:
    print("Stone paper scissor Game :")
    uwin,cwin=0,0
    for i in range(1,4):
        print("Round",i,"Start :")
        print("select an option:")
        print("1.Stone","2.paper","3.scissor",sep="\n")
        urchoice=int(input())
        if urchoice==1:
            print("u select Stone")
            urchoice="Stone"
        elif urchoice==2:
            print("u select paper")
            urchoice="paper"
        elif urchoice==3:
            print("u select scissor")
            urchoice="scissor"
        else:
            print("invalid")
        compchoice=random.choice(cchoice)
        print("computer select",compchoice)
    if urchoice==compchoice:
        print("This round is drawn:")
    elif (urchoice=="paper"and compchoice=="Stone") or (urchoice=="Stone"and compchoice=="scissor") or (urchoice=="scissor" and compchoice=="paper"):
        uwin+=1
    else:
        cwin+=1
    if uwin>cwin:
        print("you win and your score is",uwin)
    elif uwin<cwin:
        print("computer win and  score is",cwin)
    else:
        print("No one win")
    user_choice=input("want to play again?(Yes/Exit)")
    if user_choice=="yes" or user_choice=="YES" or user_choice=="Yes":  
        continue
    else:
        break

 