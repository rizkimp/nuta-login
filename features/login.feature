Feature: login
    Scenario: login
        Given visit nutapos login page
        When input valid nama perusahaan
        And input valid username
        And input valid password
        And click button login
        Then success login