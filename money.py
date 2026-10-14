import os

if os.path.exists("money.txt"):
    with open("money.txt", "r", encoding="utf-8") as file:
        money = float(file.read())
else:
    money = 0

while True:
    print(f"У тебя в копилке: {money} рублей")
    choice = input("1 — положить, 2 — забрать, 3 — выйти: ")

    if choice == "1":
        amount = float(input("Сколько положить? "))
        money += amount
        with open("money.txt", "w", encoding="utf-8") as file:
            file.write(str(money))
        print("Готово!")

    elif choice == "2":
        amount = float(input("Сколько забрать? "))
        if amount > money:
            print("Недостаточно денег")
        else:
            money -= amount
            with open("money.txt", "w", encoding="utf-8") as file:
                file.write(str(money))
            print("Готово!")

    elif choice == "3":
        print("Пока!")
        break

    else:
        print("Не понял команду")