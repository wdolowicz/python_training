# -*- coding: utf-8 -*-
__author__ = "wdolowicz"

from model.contact import Contact


def test_mod_contact_hard(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(name="test"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(name="Carl", initials="CJ", lname="Johnson", nick="CJ", title="Mr",
                      company="Rockstar Games", address="Grove Street", hphone="+199988877715",
                      mail="cj@rockstar.com", web="www.rockstargames.com")
    contact.id = old_contacts[0].id
    app.contact.modcontact(Contact())
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
