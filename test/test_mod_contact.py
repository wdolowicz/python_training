# -*- coding: utf-8 -*-
__author__ = "wdolowicz"

from model.contact import Contact
from random import randrange


def test_mod_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(name="test"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(name="Carl", initials="CJ", lname="Johnson", nick="CJ", title="Mr",
                                   company="Rockstar Games", address="Grove Street", hphone="+199988877715",
                                   mail="cj@rockstar.com", web="www.rockstargames.com")
    contact.id = old_contacts[index].id
    app.contact.modcontact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
