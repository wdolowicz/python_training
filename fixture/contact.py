__author__ = 'wdolowicz'


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        wd.get("http://localhost/addressbook/")

    def add_contact(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.name)
        self.change_field_value("middlename", contact.initials)
        self.change_field_value("lastname", contact.lname)
        self.change_field_value("nickname", contact.nick)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.hphone)
        self.change_field_value("email", contact.mail)
        self.change_field_value("homepage", contact.web)

    def create(self, new_contact_data):
        wd = self.app.wd
        self.open_home_page()
        self.add_contact()
        self.fill_contact_form(new_contact_data)
        # submit contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()


    def delete_first_contact(self):
        wd = self.app.wd
        self.open_home_page()
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # delete
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        # confirm deletion
        wd.switch_to_alert().accept()

    def delete_first_contact_hard(self):
        wd = self.app.wd
        self.open_home_page()
        # select first contact
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        # delete
        wd.find_element_by_xpath("//div[@id='content']/form[2]/input[2]").click()

    def modcontact(self, new_contact_data):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        # edit contact form
        self.fill_contact_form(new_contact_data)
        # submit contact modification
        wd.find_element_by_name("update").click()

    def modcontact_h(self, new_contact_data):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        # begin contact modification
        wd.find_element_by_name("modifiy").click()
        # edit contact form
        self.fill_contact_form(new_contact_data)
        # submit contact modification
        wd.find_element_by_name("update").click()

    def return_to_homepage(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))
