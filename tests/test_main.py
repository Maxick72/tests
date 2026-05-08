import pytest
from src.main import check_age
from src.main import check_auth
from src.main import check_triangle


@pytest.mark.parametrize(
    'age,expected_authorization',
     ((10,'Доступ запрещён'),
      (18,'Доступ разрешён'),
      (17,'Доступ запрещён'),
      (45,'Доступ разрешён'))
)
def test_check_age(age, expected_authorization):
    assert check_age(age) == expected_authorization, f'Получен неверный ответ для возраста: {age}'


@pytest.mark.parametrize(
    'login, password, expected_auth',
    (('admin', 'password', 'Добро пожаловать'),
     ('user', 'password', 'Доступ ограничен'),
     ('admin', 'P@ssw0rd', 'Доступ ограничен'))
)
def test_check_auth(login,password,expected_auth):
    assert check_auth(login, password) == expected_auth, f' Получен неверный ответ для аутентификации: {login}'


@pytest.mark.parametrize(
    'side1, side2,side3, expected_result',
    ((10,10,10,'Равносторонний треугольник'),
     (10,10,15,'Равнобедренный треугольник'),
     (10,20,15,'Разносторонний треугольник'),
     (10,20,30,'Треугольник не существует'))
)
def test_check_triangle(side1,side2,side3,expected_result):
    assert check_triangle(side1,side2,side3) == expected_result, f' Получен неверный ответ для треугольника со сторонами - {side1}:{side2}:{side3}'
