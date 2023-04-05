# Działa dla 2D6+5 i podobnych:
# liczba rzutów z przedziału 1-9
# (ale 1 musi być wpisane przez użytkownika)
# kostka typu D3, D4, D6 lub D8
# dodawana lub odejmowana liczba z przedziału 1-9
# nie obsługuje wyjątków
from random import randint


def dices(roll):
    roll_list = list(roll)
    number_of_dice_rolls = int(roll_list[0])
    type_of_dice = int(roll_list[2])
    added_number = int(roll_list[4])
    print(f"Liczba rzutów kostką: {number_of_dice_rolls}\n"
          f"Typ kostki: {type_of_dice}\n"
          f"Dodajemy (odejmujemy): {added_number}")
    result = 0
    for i in range(number_of_dice_rolls):
        result_of_roll = randint(1, type_of_dice)
        print(f"Wylosowano: {result_of_roll}")
        result += result_of_roll
    print(f"Wynik rzutu/rzutów kostką: {result}")
    if roll_list[3] == "+":
        result += added_number
    else:
        result -= added_number
    return result


your_roll = input("Wskaż rzut kostką: ")
print(f"Wynik końcowy: {dices(your_roll)}")


# xDy+z
#
# gdzie:
#
#     y – rodzaj kostek, których należy użyć (np. D6, D10),
#     x – liczba rzutów kośćmi; jeśli rzucamy raz, ten parametr jest pomijalny,
#     z – liczba, którą należy dodać (lub odjąć) do wyniku rzutów (opcjonalnie).
