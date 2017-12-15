# -*- coding: utf-8 -*-
__author__ = "wdolowicz"

from model.group import Group
from model.contact import Contact
import random


def test_add_to_group(app, orm, check_ui):
    contacts = orm.get_contact_list()
    if len(contacts) == 0:
        app.contact.create(Contact(firstname="test"))
        contacts = orm.get_contact_list()
    contact = random.choice(contacts)
    groups = orm.get_group_list()
    if len(groups) == 0:
        app.group.create(Group(name="test"))
        groups = orm.get_group_list()
    group = random.choice(groups)
    contacts_included = orm.get_contacts_in_group(group)
    app.contact.add_to_group(contact, group)
    added_contacts_in_group = orm.get_contacts_in_group(group)
    contacts_included.append(contact)
    assert sorted(contacts_included, key=Group.id_or_max) == sorted(added_contacts_in_group, key=Group.id_or_max)
    if check_ui:
        assert sorted(added_contacts_in_group, key=Group.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                              key=Group.id_or_max)
