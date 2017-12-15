__author__ = 'wdolowicz'

from model.contact import Contact
from model.group import Group
import random


def test_remove_from_group(app, orm, check_ui):
    groups = [i for i in orm.get_group_list() if i.name != ""]
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="test"))
        groups = orm.get_group_list()
    group = random.choice(groups)
    contacts_included = orm.get_contacts_in_group(group)
    if len(contacts_included) == 0:
        contacts = orm.get_contact_list()
        if len(contacts) == 0:
            app.contact.create(Contact(firstname="test"))
            contacts = orm.get_contact_list()
        contact = random.choice(contacts)
        app.contact.add_to_group(contact, group)
        contacts_included = orm.get_contacts_in_group(group)
    else:
        app.contact.select_group(group)
    contact_to_remove = random.choice(contacts_included)
    app.contact.delete_from_group(contact_to_remove, group)
    contacts_included.remove(contact_to_remove)
    new_contact_list = orm.get_contacts_in_group(group)
    assert sorted(contacts_included, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contact_list, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                         key=Contact.id_or_max)
