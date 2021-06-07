import random


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def card_chooser():
    return random.choice(cards)


def sum_of_cards(card_list):
    total = 0
    for num in card_list:
        total += num
    return total


def blackjack_game():
    your_card = []
    computer_card = []

    first_card = card_chooser()
    second_card = card_chooser()
    your_card.append(first_card)
    your_card.append(second_card)
    score = sum_of_cards(your_card)

    print(f"Your Cards: {your_card}, current score: {score} ")

    c_first_card = card_chooser()
    c_second_card = card_chooser()
    computer_card.append(c_first_card)
    computer_card.append(c_second_card)
    c_score = sum_of_cards(computer_card)
    if c_score < 17:
        c_third_card = card_chooser()
        computer_card.append(c_third_card)

    print(f"Computer's first card: {c_first_card}")

    status = input("Type 'y' to get another card, type 'n' to pass: ")
    if status == 'y':
        third_card = card_chooser()
        your_card.append(third_card)
        score = sum_of_cards(your_card)

        print(f"Your Cards: {your_card}, current score: {score} ")
        print(f"Computer's first card: {c_first_card}")
        print(f"Your Final Hand: {your_card}, final score: {score} ")
        print(f"Computer's Final Hand: {computer_card}, Final score: {c_score}")

        if score > 21:
            print("You went over! You lose 😥")
        elif score > c_score:
            print("You Win! 😀")
        elif score == c_score:
            print("Draw 😐")
        else:
            print("You lose! 😥")

    elif status == 'n':
        print(f"Your Final Hand: {your_card}, final score: {score} ")
        print(f"Computer's Final Hand: {computer_card}, Final score: {c_score}")

        if score > 21:
            print("You went over! You lose 😥")
        elif score > c_score:
            print("You Win! 😀")
        elif score == c_score:
            print("Draw 😐")
        else:
            print("You lose! 😥")


exit_status = False
while not exit_status:

    permission = input("Do you want to play a game of Blackjack? Type 'y' or 'n':  ")
    if permission == 'y':
        blackjack_game()

    elif permission == 'n':
        exit_status = True
