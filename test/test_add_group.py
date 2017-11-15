# -*- coding: utf-8 -*-
__author__ = "wdolowicz"

from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="Homework group", header="blabla", footer="blabl"))


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))
