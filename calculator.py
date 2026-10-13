number = float(input("Введите первое число: "))
operation = input("Выберите операцию (+, -, *, /): ")
second_number = float(input("Введите второе число: "))

if operation == "+":
    print(number + second_number)
elif operation == "-":
    print(number - second_number)
elif operation == "*":
    print(number * second_number)
elif operation == "/":
    if second_number == 0:
        print("На ноль делить нельзя")
    else:
        print(number / second_number)
else:
    print("Неизвестная операция")