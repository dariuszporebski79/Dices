from random import randint


def dices():
    number_of_dice_rolls = int(input("Ile razy rzucamy kostką? "))
    type_of_dice = int(input("Podaj rodzaj kostki spośród następujacych typów:\n"
                             "3, 4, 6, 8, 10, 12, 20, 100 "))
    added_number = int(input("Ile dodać lub odjąć od wyniku rzutu/ów kostką? "))
    result = 0
    for i in range(number_of_dice_rolls):
        result += randint(1, type_of_dice)
    return result + added_number


print(dices())


# roll_of_the_dice
# xDy+z
#
# gdzie:
#
#     y – rodzaj kostek, których należy użyć (np. D6, D10),
#     x – liczba rzutów kośćmi; jeśli rzucamy raz, ten parametr jest pomijalny,
#     z – liczba, którą należy dodać (lub odjąć) do wyniku rzutów (opcjonalnie).
