Scenario Outline: Add new group
  Given a group list
  Given a group with <name>, <header> and <footer>
  When I add the group to the list
  Then the new group list is equal to the old list with the added group

  Examples:
  | name  | header  | footer  |
  | name1 | header1 | footer1 |
  | name2 | header2 | footer2 |

Scenario: Delete a group
  Given a non-empty group list
  Given a random group from the list
  When I delete the group from the list
  Then the new group list is equal to the old group list without the deleted group

Scenario: Modify a group
  Given a non-empty group list
  Given a random group from the list
  Given a group with <name>, <header> and <footer>
  When I modify the group in the list
  Then the new group list is equal to the old group list with the modified group

  Examples:
  | name     | header     | footer     |
  | name_new | header_new | footer_new |