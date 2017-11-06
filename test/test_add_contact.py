# -*- coding: utf-8 -*-
__author__ = "wdolowicz"
import pytest
from fixture.application import Application
from model.contact import Contact

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(name="John", initials="JD", lname="Doe", nick="JD", title="Mr", company="Microsoft",
                               address="Redmond", hphone="+165688877744", mail="johndoe@microsoft.com",
                               web="www.johndoe.com"))
    app.session.logout()


def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(name="", initials="", lname="", nick="", title="", company="",
                               address="", hphone="", mail="", web=""))
    app.session.logout()





