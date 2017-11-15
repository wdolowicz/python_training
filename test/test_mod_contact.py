# -*- coding: utf-8 -*-
__author__ = "wdolowicz"

from model.contact import Contact


def test_mod_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(name="test"))
    app.contact.modcontact(Contact(name="Carl", initials="CJ", lname="Johnson", nick="CJ", title="Mr",
                                   company="Rockstar Games", address="Grove Street", hphone="+199988877715",
                                   mail="cj@rockstar.com", web="www.rockstargames.com"))
