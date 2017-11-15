# -*- coding: utf-8 -*-
__author__ = "wdolowicz"

from model.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact(name="John", initials="JD", lname="Doe", nick="JD", title="Mr", company="Microsoft",
                               address="Redmond", hphone="+165688877744", mail="johndoe@microsoft.com",
                               web="www.johndoe.com"))


def test_add_empty_contact(app):
    app.contact.create(Contact(name="", initials="", lname="", nick="", title="", company="",
                               address="", hphone="", mail="", web=""))





