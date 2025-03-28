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

print("Выберите операцию:")
print("1. Сложение")
print("2. Вычитание")
print("3. Умножение")
print("4. Деление")

while True:
    choice = input("Введите номер операции (1/2/3/4) или 'q' для выхода: ")
    if choice == 'q':
        break

    if choice in ('1', '2', '3', '4'):
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
            print(f"Результат: {num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            result = divide(num1, num2)
            print(f"Результат: {num1} / {num2} = {result}")
    else:
        print("Неверный ввод. Попробуйте еще раз.")

    print()  