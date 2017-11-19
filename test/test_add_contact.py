# -*- coding: utf-8 -*-
__author__ = "wdolowicz"

from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(name="John", initials="JD", lname="Doe", nick="JD", title="Mr", company="Microsoft",
                               address="Redmond", hphone="+165688877744", mail="johndoe@microsoft.com",
                               web="www.johndoe.com")
    app.contact.create(Contact())
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_add_empty_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(name="", initials="", lname="", nick="", title="", company="",
                      address="", hphone="", mail="",
                      web="")
    app.contact.create(Contact())
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)




