from model.group import Group


def test_mod_group_name(app):
    app.group.mod_first_group(Group(name="new group"))


def test_mod_group_header(app):
    app.group.mod_first_group(Group(header="new header"))
