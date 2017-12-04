__author__ = "wdolowicz"

from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 1
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(name="", initials="", lname="", nick="", title="", company="", address="", hphone="", mphone="",
                    wphone="", sphone="", mail="", web="")] + [
    Contact(name=random_string("name", 10), initials=random_string("name", 10), lname=random_string("name", 10),
            nick=random_string("name", 10), title=random_string("name", 10), company=random_string("name", 10),
            address=random_string("name", 10), hphone=random_string("name", 10), mphone=random_string("name", 10),
            wphone=random_string("name", 10), sphone=random_string("name", 10), mail=random_string("name", 10),
            web=random_string("name", 10))
    for i in range(n)
    ]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
