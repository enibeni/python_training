import pytest
from fixture.application import Application

fixture = None


@pytest.fixture  # Инициализация фикстуры
def app(request):
    global fixture
    if fixture is None:  # Самый первый раз
        fixture = Application()
    else:
        if not fixture.is_valid():  # Создае заново если сломалась
            fixture = Application()
    fixture.session.ensure_login(username="admin", password="secret")
    return fixture


@pytest.fixture(scope="session", autouse=True)  # Финализация в конце всех тестов
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture


if __name__ == '__main__':
    pytest.main()
