__author__ = 'wdolowicz'


from pytest_bdd import given, when, then
from model.contact import Contact
import random


@given('a contact list')
def contact_list(db):
    return db.get_contact_list()


@given('a contact with <firstname>, <middlename>, <lastname>, <nick>, <address>, <home>, <mobile>, <work>, <secondary>, <email>, <homepage>')
def new_contact(firstname, middlename, lastname, nick, address, home, mobile, work, secondary, email, homepage):
    return Contact(firstname=firstname, initials=middlename, lastname=lastname, nick=nick, address=address, home=home, mobile=mobile, work=work,
                   secondary=secondary, email=email, homepage=homepage)

@when('I add the contact to the list')
def add_new_contact(app, new_contact):
    app.contact.create(new_contact)

@then('the new contact list is equal to the old list with the added contact')
def verify_contact_added(db, contact_list, new_contact, app, check_ui):
    old_contacts = contact_list
    new_contacts = db.get_contact_list()
    old_contacts.append(new_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


@given('a non-empty contact list')
def non_empty_contact_list(db, app):
    if len(db.get_contact_list()) == 0:
        app.contact.add(Contact(firstname="test_contact"))
    return db.get_contact_list()


@given('a random contact from the list')
def random_contact(non_empty_contact_list):
    return random.choice(non_empty_contact_list)


@when('I delete the contact from the list')
def delete_contact(app, random_contact):
    app.contact.delete_contact_by_id(random_contact.id)
    app.wd.implicitly_wait(5)


@then('the new contact list is equal to the old list without the deleted contact')
def verify_contact_deleted(db, non_empty_contact_list, random_contact, app, check_ui):
    old_contacts = non_empty_contact_list
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(random_contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


@given('a random contact from the list')
def index_randrange_contact(non_empty_contact_list):
    return random.randrange(len(non_empty_contact_list))


@given('a contact with <firstname>, <middlename>, <lastname>, <nick>, <address>, <home>, <mobile>, <work>, <secondary>, <email>, <homepage>')
def mod_contact(firstname, middlename, lastname, nick, address, home, mobile, work, secondary, email, homepage):
    return Contact(firstname=firstname, initials=middlename, lastname=lastname, nick=nick, address=address, home=home, mobile=mobile, work=work,
                   secondary=secondary, email=email, homepage=homepage)


@when('I modify the contact in the list')
def modify_contact(app, non_empty_contact_list, index_randrange_contact, mod_contact):
    old_contacts = non_empty_contact_list
    index = index_randrange_contact
    mod_contact.id = old_contacts[index].id
    app.contact.modify_contact_by_id(mod_contact.id, mod_contact)


@then('the new contact list is equal to the old list with the modified contact')
def verify_contact_modified(app, db, non_empty_contact_list, index_randrange_contact, mod_contact, check_ui):
    old_contacts = non_empty_contact_list
    index = index_randrange_contact
    new_contacts = db.get_contact_list()
    old_contacts[index] = mod_contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
