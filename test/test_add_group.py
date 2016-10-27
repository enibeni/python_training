# -*- coding: utf-8 -*-
import pytest

from fixture.application import Application
from model.group import Group


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.add_group(Group(name="sdfg", header="sdfg", footer="sdfg"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.add_group(Group(name="", header="", footer=""))
    app.session.logout()

if __name__ == '__main__':
    pytest.main()

