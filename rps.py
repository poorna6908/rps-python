# rock-paper-scissors
print("Welcome to Rock,Paper,Scissors Game!")
user1=str(input("user1 enter  rock, paper or scissors\t"))
if (user1!="rock" and user1!= "paper" and user1!= "scissors"):
   print("Invalid Enter again")
else:
    print("Valid input")
user2=str(input("user2 enter  rock ,paper or scissors\t"))
if  (user2!="rock" and user1!="paper" and user1!= "scissors"):
    print("Invalid Enter again")
else:
    print("Valid input")



    #Battle 
if user1=="rock" and user2=="paper":
    print("user2 is the winner")
elif user1=="paper" and user2=="scissors":
    print("user2 is the winner")
elif user1==user2:
    print("Tie")
else:
    print("user1 is the winner")
