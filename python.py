import random
def game():
    randomN=random.randint(0,50)
    def run(a,limit,count=0):
        b=True
        
        answer=int(input(" Guess no. Between(0,50): "))
        if(count<limit):
            if(answer==a):
                print("🙌 Winner 🎉")
                b=True
            else:
                b=False
                if(answer > a):
                    print("🤡 Hint: random number is less than Your no.!")
                else:
                    print("🤡 Hint: random number is greater than Your no.!")
                run(a,limit,count+1)

        

    print("...~~~~~~~Guess Number Game~~~~~~~... ")
    yesno=input(" 👀 Want to play: ")
    if(yesno.lower()=="yes"):
        run(randomN,5)
    else:
        print("Quit")
game()        