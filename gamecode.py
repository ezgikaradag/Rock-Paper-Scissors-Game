import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''


paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''


scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print("What do you choice? Type 0 for Rock, 1 for Paper, 2 for Scissors.")

game_images = [rock,paper,scissors]
userchoice = int(input())
print(game_images[userchoice])
computerChoice = random.randint(0,2)
print(game_images[computerChoice]) 

print(f"Your choice {userchoice}")
print(f"Computer choice {computerChoice}\n")

      if userchoice >= 3 or  userchoice < 0:
        print("You typed an invalid number.You lose! :(") 
      elif userchoice==2 and computerChoice == 0:
        print("You lose! :(")
      elif computerChoice==2 and userchoice == 0:
       print("You win! :)")
      elif computerChoice > userchoice:
       print("You lose! :(")
      elif userchoice > computerChoice:
       print("You win! :)")
      elif computerChoice==userchoice:
       print("It's a draw. :|")

 
 
