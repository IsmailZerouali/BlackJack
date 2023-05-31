
from art import logo
import random
import replit

def score():
  print(f"    Your cards: {your_list}, current score: {sum(your_list)}")
  print(f"    Computer's first card: {comp_card1}")
  
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

switch2 = False
while not switch2:
  answer = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
  
  if answer == "y":
    replit.clear()
    print(logo)
    
    first_card = random.choice(cards)
    second_card = random.choice(cards)
    comp_card1 = random.choice(cards)
    comp_card2 = random.choice(cards)
    your_list = [first_card, second_card]
    comp_list = [comp_card1, comp_card2]
    
    score()
    
    switch1 = False
    while not switch1:
      other = input("Type 'y' to get another card, type 'n' to pass: ").lower()
      if other == "y":
        your_list.append(random.choice(cards))
        score()
        
      elif other == "n":
        switch1 = True
        while sum(comp_list) < 16 :
            comp_list.append(random.choice(cards))
          
    print(f"Your final hand: {your_list}, final score: {sum(your_list)}")
    print(f"Computer's final hand: {comp_list}, final score: {sum(comp_list)}")
    
    your_sum = sum(your_list)
    comp_sum = sum(comp_list)
    
    if your_sum == comp_sum:
      print("Draw!")
      
    else:
      if your_sum >21:
        if comp_sum >21:
          if your_sum < comp_sum:
            print("You win! :D")
          else:
            print("You lose! :D")
        else:
          print("You lose! :D")
      else:
        if comp_sum >21:
          print("You lose! :D")
        else:
          if your_sum > comp_sum:
            print("You win! :D")
          else:
            print("You lose! :D")
  else:
    switch2 = True
    print("See you soon! :D")
