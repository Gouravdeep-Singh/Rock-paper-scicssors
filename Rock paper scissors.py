#Make a two-player Rock-Paper-Scissors game.
#(Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)
#Remember the rules:

#Rock beats scissors
#Scissors beats paper
#Paper beats rock

def task():
    x=input("enter your choice player 1")
    y=input("enter your choice player 2")
    if (x=="rocks" and y=="scissors") or (x=="scissors" and y=="paper") or (x=="paper" and y=="rock"):
       print("x wins")
    elif x==y:
       print("draw")
    elif (y=="rocks" and x=="scissors") or (y=="scissors" and x=="paper") or (y=="paper" and x=="rock"):
       print("y wins")
    else:
       print("invalid input")


task()
c="yes"
while c=="yes":
    print("Continue playing? yes or No:")
    c=input()
    if c=="yes":
        task()
