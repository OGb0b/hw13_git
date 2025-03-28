import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Ошибка: деление на ноль!"
    return a / b

def power(a, b):
    return a ** b

def square_root(a):
    if a < 0:
        return "Ошибка: корень из отрицательного числа!"
    return math.sqrt(a)

def factorial(a):
    if a < 0:
        return "Ошибка: факториал отрицательного числа!"
    return math.factorial(int(a))

def round_num(a, decimals=0):
    return round(a, decimals)

print("Выберите операцию:")
print("1. Сложение")
print("2. Вычитание")
print("3. Умножение")
print("4. Деление")
print("5. Возведение в степень")
print("6. Квадратный корень")
print("7. Факториал")
print("8. Округление числа")

while True:
    choice = input("\nВведите номер операции (1-8) или 'q' для выхода: ").strip()
    
    if choice == 'q':
        break

    if choice in ('1', '2', '3', '4', '5'):
        try:
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))
        except ValueError:
            print("Ошибка: введите числа!")
            continue

        if choice == '1':
            print(f"Результат: {num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"Результат: {num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"Результат: {num1} × {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            result = divide(num1, num2)
            print(f"Результат: {num1} ÷ {num2} = {result}")
        elif choice == '5':
            print(f"Результат: {num1} ^ {num2} = {power(num1, num2)}")

    elif choice in ('6', '7', '8'):
        try:
            num = float(input("Введите число: "))
        except ValueError:
            print("Ошибка: введите число!")
            continue

        if choice == '6':
            result = square_root(num)
            print(f"√{num} = {result}")
        elif choice == '7':
            result = factorial(num)
            print(f"{num}! = {result}")
        elif choice == '8':
            decimals = int(input("Введите количество знаков после запятой: "))
            print(f"{num} округлённое = {round_num(num, decimals)}")
    else:
        print("Неверный ввод. Попробуйте ещё раз.")