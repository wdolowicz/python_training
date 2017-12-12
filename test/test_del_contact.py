__author__ = "wdolowicz"
from model.contact import Contact
import random

def test_del_some_contact(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(name="test"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
