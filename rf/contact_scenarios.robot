*** Settings ***
Library  rf.Addressbook
Library  Collections
Suite Setup  Init Fixtures
Suite Teardown  Destroy Fixtures


*** Test Cases ***
Add new contact
    ${old_list}=  Get Contact List
    ${contact}=  New Contact  firstname_1  initials_1  lastname_1  nick_1  title_1  company_1  address_1  home_1  mobile_1  work_1  secondary_1  email_1  email2_1  email3_1  homepage_1
    Add Contact  ${contact}
    ${new_list}=  Get Contact List
    Append To List  ${old_list}  ${contact}
    Contact Lists Should Be Equal  ${new_list}  ${old_list}

Delete contact
    ${old_list}=  Get Contact List
    ${len}=  Get Length  ${old_list}
    ${test_contact}=  New Contact  firstname_t  initials_t  lastname_t  nick_t  title_t  company_t  address_t  home_t  mobile_t  work_t  secondary_t  email_t  email2_t  email3_t  homepage_t
    Run Keyword If  ${len}== 0  Add Contact  ${test_contact}
    ${old_list}=  Get Contact List
    ${len}=  Get Length  ${old_list}
    ${index}=  Evaluate  random.randrange(${len})  random
    ${contact}=  Get From List  ${old_list}  ${index}
    Delete Contact  ${contact}
    ${new_list}=  Get Contact List
    Remove Values From List  ${old_list}  ${contact}
    Contact Lists Should Be Equal  ${new_list}  ${old_list}

Modify contact
    ${old_list}=  Get Contact List
    ${len}=  Get Length  ${old_list}
    ${test_contact}=  New Contact  firstname_t  initials_t  lastname_t  nick_t  title_t  company_t  address_t  home_t  mobile_t  work_t  secondary_t  email_t  email2_t  email3_t  homepage_t
    Run Keyword If  ${len}== 0  Add Contact  ${test_contact}
    ${old_list}=  Get Contact List
    ${len}=  Get Length  ${old_list}
    ${index}=  Evaluate  random.randrange(${len})  random
    ${source_contact}=  Get From List  ${old_list}  ${index}
    ${new_data_contact}=  New Contact  firstname_mod  initials_mod  lastname_mod  nick_mod  title_mod  company_mod  address_mod  home_mod  mobile_mod  work_mod  secondary_mod  email_mod  email2_mod  email3_mod  homepage_mod
    Modify Contact  ${source_contact}  ${new_data_contact}
    ${new_list}=  Get Contact List
    Set List Value  ${old_list}  ${index}  ${new_data_contact}
    Contact Lists Should Be Equal  ${new_list}  ${old_list}