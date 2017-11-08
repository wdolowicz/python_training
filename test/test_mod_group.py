# -*- coding: utf-8 -*-
__author__ = "wdolowicz"

from model.group import Group


def test_mod_group(app):
    app.session.login(username="admin", password="secret")
    app.group.mod_first_group(Group(name="Edited group", header="hello", footer="world"))
    app.session.logout()