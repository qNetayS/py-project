import random

with open('111.txt', 'r') as file:
    lines = file.readlines()
    stone = int(lines[0])
    scissors = int(lines[1])
    paper = int(lines[2])
    player_score = int(lines[3])
    ii_score = int(lines[4])

def main_round(a, b):
    if a not in ["бумага", "камень", "ножницы"] or b not in ["бумага", "камень", "ножницы"]:
        return "Ошибка: недопустимый вариант"
    elif (a == "бумага" and b == "ножницы") or (a == "камень" and b == "бумага") or (a == "ножницы" and b == "камень"):
        return "бот выйграл"
    elif (a == "бумага" and b == "бумага") or (a == "ножницы" and b == "ножницы") or (a == "камень" and b == "камень"):
        return "ничья"
    else:
        return "вы выйграли"

def main_prog():
    num = random.randint(1, stone + scissors + paper)
    if num <= stone:
        sch = "камень"
    elif num > stone and num <= stone + scissors:
        sch = "ножницы"
    else:
        sch = "бумага"
    return sch

def main():
    global stone, scissors, paper, player_score, ii_score
    a = input("Выберите бумагу, камень или ножницы (для выхода введите 'выход'): ")
    if a == "выход":
        return # условие выхода из рекурсии
    if a == "ножницы":
        scissors -= 3
        stone += 6
        paper -= 3
    elif a == "камень":
        scissors -= 3
        stone -= 3
        paper += 6
    else:
        scissors += 6
        stone -= 3
        paper -= 3

    b = main_prog()
    result = main_round(a, b)
    print("Бот выбрал:", b)
    print("Результат:", result)
    if result == "бот выйграл":
        ii_score += 1
    elif result == "вы выйграли":
        player_score += 1

    print("Текущий счет:")
    print("Игрок:", player_score)
    print("Бот:", ii_score)

    with open('111.txt', 'w') as file:
        file.write(str(stone) + "\n")
        file.write(str(scissors) + "\n")
        file.write(str(paper) + "\n")
        file.write(str(player_score) + "\n")
        file.write(str(ii_score) + "\n")
    main()

main()
