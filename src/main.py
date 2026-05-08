def check_age(age: int):

    if age >= 18:
        result = 'Доступ разрешён'
    else:
        result = 'Доступ запрещён'

    return result

def check_auth(login: str, password: str):

    if login == 'admin' and password == 'password':
           result = 'Добро пожаловать'
    else:
           result = 'Доступ ограничен'

    return result

def check_triangle(side1: int, side2: int, side3: int):
    if (side1 + side2) <= side3 or (side2 + side3) <= side1 or (side1 + side3) <= side2  :
        result = "Треугольник не существует"
    elif side1 == side2 == side3:
        result = "Равносторонний треугольник"
    elif side1 == side2 or side1 == side3 or side2 == side3:
        result = "Равнобедренный треугольник"
    else:
        result = "Разносторонний треугольник"
    return result

