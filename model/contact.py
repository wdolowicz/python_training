__author__ = 'wdolowicz'

from sys import maxsize


class Contact:
    def __init__(self, name=None, initials=None, lname=None, nick=None, title=None, company=None, address=None,
                 hphone=None, mphone=None, wphone=None, sphone=None, mail=None, mail2=None, mail3=None, web=None,
                 all_phones_from_home_page=None, all_email_from_home_page=None, id=None):
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
        self.mail2 = mail2
        self.mail3 = mail3
        self.web = web
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_email_from_home_page = all_email_from_home_page

    def __repr__(self):
        return "%s:%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s" % (self.id, self.name, self.lname, self.initials, self.nick,
                                                              self.title, self.company, self.address, self.hphone,
                                                              self.mphone, self.wphone, self.sphone, self.mail,
                                                              self.web)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) \
               and self.name == other.name and self.lname == other.lname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
