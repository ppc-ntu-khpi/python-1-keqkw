def sqrPlus1(x):
    return x**2 + 1

numbers = []
n = 1
while n <= 10:
    x = int(input(str(n) + " - введіть число від 0 до 10:"))
    if 0 <= x <= 10:
        numbers.append(sqrPlus1(x))
        n += 1
    else:
        print("Потрібне число від 0 до 10!")
print("Результат для Завдання 1:", numbers)

add = lambda a, b: a + b
sub = lambda a, b: a - b
mul = lambda a, b: a * b
div = lambda a, b: a / b if b != 0 else 0

a = int(input("Введіть перше число:"))
b = int(input("Введіть друге число:"))

menu = {
    '1': "Додати числа",
    '2': "Відняти числа",
    '3': "Перемножити числа",
    '4': "Поділити числа",
    '5': "завершити роботу"
}

for entry, description in menu.items():
    print(entry, description)

while True:
    selection = input("Оберіть операцію:")
    if selection == '1':
        print("Додавання:", add(a, b))
    elif selection == '2':
        print("Віднімання:", sub(a, b))
    elif selection == '3':
        print("Множення:", mul(a, b))
    elif selection == '4':
        print("Ділення:", div(a, b))
    elif selection == '5':
        break
    else:
        print("Невідома операція!")

def controlEngine(id, name, operation="стоп", priority="високий"):
    print('Агрегат:', name, '#', id, "\n\tОбрана операція:", operation, "\n\tПриорітет:", priority)

controlEngine(1, "реактор")
controlEngine(1, "реактор", "запуск")
controlEngine(1, "реактор", priority="звичайний")
controlEngine(operation="запуск", id=1, name="реактор", priority="звичайний")
