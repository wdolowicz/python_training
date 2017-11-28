__author__ = 'wdolowicz'

from sys import maxsize

class Contact:
    def __init__(self, name=None, initials=None, lname=None, nick=None, title=None, company=None, address=None,
                 hphone=None, mphone=None, wphone=None, sphone=None, mail=None, web=None, id=None):
        self.name = name
        self.initials = initials
        self.lname = lname
        self.nick = nick
        self.title = title
        self.company = company
        self.address = address
        self.hphone = hphone
        self.mphone = mphone
        self.wphone = wphone
        self.sphone = sphone
        self.mail = mail
        self.web = web
        self.id = id



    def __repr__(self):
        return "%s" % (self.id)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
