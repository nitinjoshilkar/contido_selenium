Feature: Verifying Login page functionality



Scenario Outline: verify user login with valid credentials

	Given User Launches Chrome browser
	When User opens URL "https://dyn.stg.contido.io/login"
	And User enters Email as "<username>" and Password as "<password>"
	And user clicks on login
	Then User should be able to login to application
	And User should be on Homepage of the application.
    And Logout the application
	And close browser

	Examples:
		| username              | password      |
		| opsuser@desynova.com  | dyn@opsuser20 |

