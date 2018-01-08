*** Settings ***
Library  rf.Addressbook
Library  Collections
Suite Setup  Init Fixtures
Suite Teardown  Destroy Fixtures


*** Test Cases ***
Add new group
    ${old_list}=  Get Group List
    ${group}=  New Group  name1  header1  footer1
    Create Group  ${group}
    ${new_list}=  Get Group List
    Append to list  ${old_list}  ${group}
    Group Lists Should Be Equal  ${new_list}  ${old_list}

Delete group
    ${old_list}=  Get Group List
    ${len}=  Get Length  ${old_list}
    ${index}=  Evaluate  random.randrange(${len})  random
    ${group}=  Get From List  ${old_list}  ${index}
    Delete Group  ${group}
    ${new_list}=  Get Group List
    Remove Values From List  ${old_list}  ${group}
    Group Lists Should Be Equal  ${new_list}  ${old_list}

Modify group
    ${old_list}=  Get Group List
    ${len}=  Get Length  ${old_list}
    ${index}=  Evaluate  random.randrange(${len})  random
    ${source_group}=  Get From List  ${old_list}  ${index}
    ${new_data_group}=  New Group  name_mod  header_mod  footer_mod
    Modify Group  ${source_group}  ${new_data_group}
    ${new_list}=  Get Group List
    Set List Value  ${old_list}  ${index}  ${new_data_group}
    Group Lists Should Be Equal  ${new_list}  ${old_list}