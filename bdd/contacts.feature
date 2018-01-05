Scenario Outline: Add new contact
  Given a contact list
  Given a contact with <firstname>, <middlename>, <lastname>, <nick>, <address>, <home>, <mobile>, <work>, <secondary>, <email>, <homepage>
  When I add the contact to the list
  Then the new contact list is equal to the old list with the added contact

  Examples:
  | firstname  | middlename  | lastname  | nick  | address  | home  | mobile  | work  | secondary  | email  | homepage  |
  | firstname1 | middlename1 | lastname1 | nick1 | address1 | home1 | mobile1 | work1 | secondary1 | email1 | homepage1 |
  | firstname2 | middlename2 | lastname2 | nick2 | address2 | home2 | mobile2 | work2 | secondary2 | email2 | homepage2 |


Scenario: Delete a contact
  Given a non-empty contact list
  Given a random contact from the list
  When I delete the contact from the list
  Then the new contact list is equal to the old list without the deleted contact


Scenario: Modify a contact
  Given a non-empty contact list
  Given a random contact from the list
  Given a contact with <firstname>, <middlename>, <lastname>, <nick>, <address>, <home>, <mobile>, <work>, <secondary>, <email>, <homepage>
  When I modify the contact in the list
  Then the new contact list is equal to the old list with the modified contact

  Examples:
  | firstname     | middlename   | lastname     | nick     | address     | home     | mobile     | work     | secondary   | email     | homepage   |
  | firstname_mod | middlename_m | lastname_mod | nick_mod | address_mod | home_mod | mobile_mod | work_mod | secondary_m | email_mod | homepage_m |