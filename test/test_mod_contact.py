# -*- coding: utf-8 -*-
__author__ = "wdolowicz"

from model.contact import Contact
from random import randrange


def test_mod_contact(app, db, check_ui):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="Carl", initials="CJ", lastname="Johnson", nick="CJ", title="Mr", company="Rockstar Games",
                      address="Grove Street", home="+199988877715", mobile="+1434376655683", work="+13475674567456",
                      secondary="+15643657456485", email="cj@rockstar.com", homepage="www.rockstargames.com")
    contact.id = old_contacts[index].id
    app.contact.modcontact_by_index(index, contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.group.get_contact_list(), key=Contact.id_or_max)
