# -*- coding: utf-8 -*-
__author__ = 'wdolowicz'

import re

def test_phones_on_homepage(app):
    contact_from_homepage = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_homepage.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)

def test_email_on_homepage(app):
    contact_from_homepage = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_homepage.all_email_from_home_page == merge_email_like_on_home_page(contact_from_edit_page)

def test_names_and_address_on_homepage(app):
    contact_from_homepage = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_homepage.name == contact_from_edit_page.name
    assert contact_from_homepage.lname == contact_from_edit_page.lname
    assert contact_from_homepage.address == contact_from_edit_page.address

def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.hphone == contact_from_edit_page.hphone
    assert contact_from_view_page.mphone == contact_from_edit_page.mphone
    assert contact_from_view_page.wphone == contact_from_edit_page.wphone
    assert contact_from_view_page.sphone == contact_from_edit_page.sphone

def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.hphone, contact.mphone, contact.wphone, contact.sphone]))))

def merge_email_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.mail, contact.mail2, contact.mail3]))))