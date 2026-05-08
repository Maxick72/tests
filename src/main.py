

def check_age(age: int):

    if age >= 18:
        result = 'Доступ разрешён'
    else:
        result = 'Доступ запрещён'

    return result

def check_auth(login: str, password: str):

    if login == 'admin' and password == 'password':# Здесь напишите свой код для проверки условия
           result = 'Добро пожаловать'    # В этом блоке напишите код, который выполнится, если условие True. Используйте result, как в задании выше
    else:
           result = 'Доступ ограничен'# В этом блоке напишите код, который выполнится, если условие False. Используйте result, как в задании выше

    return result

def check_triangle(side1: int, side2: int, side3: int):
    if (side1 + side2) <= side3 or (side2 + side3) <= side1 or (side1 + side3) <= side2  : # условие, что треугольник не существует
        result = "Треугольник не существует"
    elif side1 == side2 == side3: # условие, что треугольник равносторонний
        result = "Равносторонний треугольник"
    elif side1 == side2 or side1 == side3 or side2 == side3: # условие, что треугольник равнобедренный
        result = "Равнобедренный треугольник"
    else: # во всех остальных случаях треугольник разносторонний
        result = "Разносторонний треугольник"
    return result
