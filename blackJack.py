import random
playerIn=True
dealerIn=True
# deck of cards / player dealer hand
deck=[2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
      'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A']
playerHand=[]
dealerHand=[]
# deal the cards
def dealCard(turn):
    card=random.choice(deck)
    turn.append(card)
    deck.remove(card)
# calculate the total of each hand
def total(hand):
    total = 0
    ace_11s = 0
    for card in hand:
        if card in range(11):
            total += card
        elif card in ['J', 'K', 'Q']:
            total += 10
        else:
            total += 11
            ace_11s += 1
    while ace_11s and total > 21:
        total -= 10
        ace_11s -= 1
    return total
# check for winner
def revealDealerHand():
    if len(dealerHand)==2:
        return dealerHand[0]
    elif len(dealerHand)>2:
        return dealerHand[0], dealerHand[1]

# game loop
for _ in range(2):
    dealCard(dealerHand)
    dealCard(playerHand)

while playerIn or dealerIn:
    print(f"Dealer had{revealDealerHand()} and X")
    print(f"You have{playerHand} for a total of {total(playerHand)}")
    if playerIn:
        stayOrHit = input("1: Stay\n2: Hit\n")
    if total(dealerHand) > 17:
        dealerIn=False
    else:
        dealCard(dealerHand)
    if stayOrHit=='1':
        playerIn=False
    else:
        dealCard(playerHand)
    if total(playerHand)>=21:
        break
    elif total(dealerHand)>=21:
        break
if total(playerHand)==21:
    print(f"\nYou have {playerHand} for a total of {total(playerHand)} and a dealer has {dealerHand} for a total of {total(dealerHand)}")
    print("It's Blackjack, You win!!!")
elif total(dealerHand)==21:
    print(f"\nYou have {playerHand} for a total of {total(playerHand)} and a dealer has {dealerHand} for a total of {total(dealerHand)}")
    print("It's Blackjack, Dealer wins!!!")
elif total(playerHand)>21:
    print(f"\nYou have {playerHand} for a total of {total(playerHand)} and a dealer has {dealerHand} for a total of {total(dealerHand)}")
    print("You busted, Dealer wins!!!")
elif total(dealerHand)>21:
    print(f"\nYou have {playerHand} for a total of {total(playerHand)} and a dealer has {dealerHand} for a total of {total(dealerHand)}")
    print("Dealer busted, You win!!!")
elif 21 - total(dealerHand) < 21 - total(playerHand):
    print(f"\nYou have {playerHand} for a total of {total(playerHand)} and a dealer has {dealerHand} for a total of {total(dealerHand)}")
    print("Dealer wins!!!")
elif 21 -total(dealerHand) > 21 - total(playerHand):
    print(f"\nYou have {playerHand} for a total of {total(playerHand)} and a dealer has {dealerHand} for a total of {total(dealerHand)}")
    print("You win!!!")