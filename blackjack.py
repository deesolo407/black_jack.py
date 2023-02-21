print ("Dee's BlackJack")
print ("     .------..------..------..------..------.      .------..------..------..------. ")
print ("     |B.--. ||L.--. ||A.--. ||C.--. ||K.--. |.-.   |J.--. ||A.--. ||C.--. ||K.--. | ")
print ("     | :(): || :/\: || (\/) || :/\: || :/\: |((5)) | :(): || (\/) || :/\: || :/\: | ")
print ("     | ()() || (__) || :\/: || :\/: || :\/: |'-.-. | ()() || :\/: || :\/: || :\/: | ")
print ("     | '--'B|| '--'L|| '--'A|| '--'C|| '--'K| ((1))| '--'J|| '--'A|| '--'C|| '--'K| ")
print ("     `------'`------'`------'`------'`------' '-'  `------'`------'`------'`------' ")

import random

def draw_card():
    return random.randint(1, 11)

def play_blackjack():
    print("let's play Blackjack!")
    player_hand = [draw_card(), draw_card()]
    dealer_hand = [draw_card(), draw_card()]
    
    print("Your hand: ", player_hand)
    print("Dealer's hand: ", dealer_hand[0], "???")
    
    while sum(player_hand) < 21:
        action = input("Do you want to hit, stand, double down, or split? ")
        if action == "hit":
            player_hand.append(draw_card())
            print("Your hand: ", player_hand)
        elif action == "stand":
            break
        elif action == "double down":
            player_hand.append(draw_card())
            print("Your hand: ", player_hand)
            break
        elif action == "split":
            split_hand = [player_hand.pop()]
            player_hand.append(draw_card())
            split_hand.append(draw_card())
            print("Your hand: ", player_hand)
            print("Split hand: ", split_hand)
            while sum(split_hand) < 21:
                split_action = input("Do you want to hit or stand on split hand? ")
                if split_action == "hit":
                    split_hand.append(draw_card())
                    print("Split hand: ", split_hand)
                elif split_action == "stand":
                    break
                else:
                    print("Invalid action. Try again.")
        else:
            print("Invalid action. Try again.")
            
    if sum(player_hand) > 21:
        print("You busted with a hand of ", player_hand, ". Better luck next time!")
        return
    
    while sum(dealer_hand) < 17:
        dealer_hand.append(draw_card())
    
    if sum(dealer_hand) > 21:
        print("Dealer busted with a hand of ", dealer_hand, ". You win!")
    elif sum(dealer_hand) > sum(player_hand):
        print("Dealer wins with a hand of ", dealer_hand, ".")
    elif sum(dealer_hand) < sum(player_hand):
        print("You win with a hand of ", player_hand, ".")
    else:
        print("It's a tie with hands of ", player_hand, "and", dealer_hand, ".")
     
    print("Dee's BlackJack")      
     
play_blackjack()
    