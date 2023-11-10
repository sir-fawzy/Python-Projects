from random import randint
def draw(num):
    if num == 1:
        return "Drew an Ace"
    elif 2<=num <= 10:
        if num == 8:
            return f"Drew an {num}" 
        else:
            return f"Drew a {num}"
    elif num == 11:
        return f"Drew a Jack"
    elif num == 12:
        return f"Drew a Queen"
    elif num == 13:
        return f"Drew a King"
    else:
        return "BAD CARD"
    
def card_value(num):
    if num > 13 or num <1:
        return "BAD CARD"
    
    elif num in [11, 12, 13]:
        return 10
    elif num == 1 :
        return 11
    else:
        return num
    
def blackjack_or_bust(hand):
    if hand < 4 or hand > 31 :
        return "BAD HAND VALUE!"
    elif hand == 21:
        return "BLACKJACK!"
    elif hand > 21:
        return "BUST."
    else:
        return None


# Write all of your part 2A code below this comment. DO NOT CHANGE OR REMOVE THIS COMMENT.
def play_dealer_turn():
    hand_value = 0
    counter = 0
    while counter < 2:
        choice = randint(1, 13)
        print(draw(choice))
        hand_value += card_value(choice)
        counter += 1

    if hand_value< 17:
        print(f"Dealer has {hand_value}.")

    while hand_value < 17:
        choice = randint(1, 13)
        print(draw(choice))
        hand_value += card_value(choice)
        if hand_value< 17:
            print(f"Dealer has {hand_value}.")

        
    if hand_value == 21:
        print(f"Final hand: {hand_value}.")
        print("BLACKJACK!")
    elif hand_value > 21:
        print(f"Final hand: {hand_value}.")
        print("BUST.")
    else:
        print(f"Final hand: {hand_value}.")


# Write all of your part 2B code below this comment. DO NOT CHANGE OR REMOVE THIS COMMENT.
def play_human_turn():
    hand_value = 0
    starting = 0
    while starting < 2:
        choice = randint(1, 13)
        print(draw(choice))
        hand_value += card_value(choice)
        starting += 1

    while hand_value < 21:
        hit = input(f"You have {hand_value}. Hit (y/n)? ")
        if hit.strip().lower() == "y" or hit.strip().lower() == "yes" :
            choice = randint(1, 13)
            print(draw(choice))
            hand_value += card_value(choice)
        elif hit.strip().lower() == "n" or hit.strip().lower() == "no":
            break
        else:
            print("Sorry I didn't get that.")
            continue
    print(f"Final hand: {hand_value}.")
    if blackjack_or_bust(hand_value) != None:
        print(blackjack_or_bust(hand_value))

play_human_turn()