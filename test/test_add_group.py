# -*- coding: utf-8 -*-
__author__ = "wdolowicz"

from model.group import Group


def test_add_group(app):
    old_groups = app.group.get_group_list()
    group = Group(name="Homework group", header="blabla", footer="blabl")
    app.group.create(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    assert old_groups == new_groups


#def test_add_empty_group(app):
#    old_groups = app.group.get_group_list()
#    app.group.create(Group(name="", header="", footer=""))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) + 1 == len(new_groups)