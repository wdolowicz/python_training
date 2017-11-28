# -*- coding: utf-8 -*-
__author__ = 'wdolowicz'

import re

def test_phones_on_homepage(app):
    contact_from_homepage = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_homepage.hphone == clear(contact_from_edit_page.hphone)
    assert contact_from_homepage.mphone == clear(contact_from_edit_page.mphone)
    assert contact_from_homepage.wphone == clear(contact_from_edit_page.wphone)
    assert contact_from_homepage.sphone == clear(contact_from_edit_page.sphone)

def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.hphone == contact_from_edit_page.hphone
    assert contact_from_view_page.mphone == contact_from_edit_page.mphone
    assert contact_from_view_page.wphone == contact_from_edit_page.wphone
    assert contact_from_view_page.sphone == contact_from_edit_page.sphone

def clear(s):
    return re.sub("[() -]", "", s)