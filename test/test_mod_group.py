from model.group import Group


def test_mod_group_name(app):
    old_group = app.group.get_group_list()
    group = Group(name="new group")
    group.id = old_group[0].id
    app.group.mod_first_group(group)
    new_group = app.group.get_group_list()
    assert len(old_group) == len(new_group)
    old_group[0] = group
    assert sorted(old_group, key = Group.id_or_max) == sorted(new_group, key = Group.id_or_max)


# def test_mod_group_header(app):
#     app.group.mod_first_group(Group(header="new header"))
