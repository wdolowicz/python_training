# -*- coding: utf-8 -*-
__author__ = "wdolowicz"

from model.contact import Contact


def test_mod_contact(app):
    app.contact.modcontact(Contact(name="Carl", initials="CJ", lname="Johnson", nick="CJ", title="Mr", company="Rockstar Games",
                                   address="Grove Street", hphone="+199988877715", mail="cj@rockstar.com",
                                   web="www.rockstargames.com"))
