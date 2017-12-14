__author__ = 'wdolowicz'

from sys import maxsize


class Contact:
    def __init__(self, firstname=None, initials=None, lastname=None, nick=None, title=None, company=None, address=None,
                 home=None, mobile=None, work=None, secondary=None, email=None, email2=None, email3=None, homepage=None,
                 all_phones_from_home_page=None, all_email_from_home_page=None, id=None):
        self.firstname = firstname
        self.initials = initials
        self.lastname = lastname
        self.nick = nick
        self.title = title
        self.company = company
        self.address = address
        self.home = home
        self.mobile = mobile
        self.work = work
        self.secondary = secondary
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_email_from_home_page = all_email_from_home_page

    def __repr__(self):
        return "%s:%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s" % (self.id, self.firstname, self.lastname, self.initials, self.nick,
                                                              self.title, self.company, self.address, self.home,
                                                              self.mobile, self.work, self.secondary, self.email,
                                                              self.homepage)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) \
               and self.firstname == other.firstname and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
