deck = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
choice = 0
player = []
dealer = []


def deck_total(person):
    res = 0
    check_ACE = 0
    i = 0

    while i < len(person):
        try:
            res += int(person[i])
        except:
            if person[i] == "A":
                check_ACE = 1
            else:
                res += 11
        i += 1

    if check_ACE == 1:
        if (res + 10) > 21:
            res += 1
        else:
            res += 11
    return res


def hand_value(player, dealer):

    print("Dealer's total is: " + str(deck_total(dealer)) + " →")
    i = 0
    while i < len(dealer):
        print(dealer[i], end="")
        i += 1
        if i < len(dealer):
            print(", ", end="")

    print("\nPlayer's total is: " + str(deck_total(player)) + " →")
    i = 0
    while i < len(player):
        print(player[i], end="")
        i += 1
        if i < len(player):
            print(", ", end="")
    return 0


import random

random.shuffle(deck)
print("Dealer draws first card")
dealer.append(deck[0])
del deck[0]
print("Player receives two cards\n")
player.append(deck[0])
del deck[0]
player.append(deck[0])
del deck[0]
hand_value(player, dealer)

while choice != "S" and choice != "s":
    choice = input("\n\nDo you want to (H)it, (S)tand, or (Q)uit?\n")

    if choice == "H" or choice == "h":
        if len(deck) != 0:
            player.append(deck[0])
            del deck[0]
        hand_value(player, dealer)

        if deck_total(player) > 21:
            print("\n\nYou bust! You lost the game.")
            input('Press ENTER to exit')
            exit()

    elif choice == "Q" or choice == "q":
        exit()

while int(deck_total(dealer)) < 17:
    dealer.append(deck[0])
    del deck[0]

hand_value(player, dealer)
print("\n")

if deck_total(dealer) > 21:
    print("Dealer busts! You Win!")
elif deck_total(dealer) > deck_total(player):
    print("Dealer wins!")
elif deck_total(dealer) < deck_total(player):
    print("You win!")
else:
    print("Tie!")

input('Press any key to exit')