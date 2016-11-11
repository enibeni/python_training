import pytest
import string
import random
from model.group import Group

def random_string(prefix, maxlem):
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlem))])


testdata = [Group(name="", header="header", footer="footer")] + [
        Group(name=random_string("name", 10), header=random_string("header", 10), footer=random_string("footer", 10))
        for i in range(5)
]


@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_mod_random_group_name(app, group):
    old_groups = app.group.get_group_list()
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count() # Хэш фунция
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(new_groups, key = Group.id_or_max) == sorted(old_groups, key = Group.id_or_max)



# def test_add_empty_group(app):
#     old_groups = app.group.get_group_list()
#     group = Group(name="", header="", footer="")
#     app.group.create(group)
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) + 1 == len(new_groups)
#     old_groups.append(group)
#     assert sorted(new_groups, key=Group.id_or_max) == sorted(old_groups, key=Group.id_or_max)





