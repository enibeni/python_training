from model.group import Group


def test_mod_random_group_name(app, db, json_groups):
    group = json_groups
    old_groups = db.get_group_list()
    app.group.create(group)
    new_groups = db.get_group_list()
    old_groups.append(group)
    assert sorted(new_groups, key = Group.id_or_max) == sorted(old_groups, key = Group.id_or_max)





