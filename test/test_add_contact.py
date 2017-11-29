# -*- coding: utf-8 -*-
__author__ = "wdolowicz"

from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(name="", initials="", lname="", nick="", title="", company="", address="", hphone="", mphone="",
                    wphone="", sphone="", mail="", web="")] + [
    Contact(name=random_string("name", 10), initials=random_string("initials", 2), lname=random_string("lname", 10),
            nick=random_string("nick", 10), title=random_string("title", 3), company=random_string("company", 20),
            address=random_string("address", 30), hphone=random_string("hphone", 9), mphone=random_string("mphone", 9),
            wphone=random_string("wphone", 9), sphone=random_string("sphone", 9), mail=random_string("mail", 15),
            web=random_string("web", 20))
    for i in range(5)
    ]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
