###Automation of automationpractice.com site
+ For Single file run in terminal command is:</br>
 ``pytest -s -v "filename with extention"``
+ For while tests are run in terminal command ia: </br>
``pytest -s -v``
+ Run mark file:</br>
``pytest -m "marker name" "file name"``


####Package description
- ***PageObject:*** All pages are available in this package and all locator and methods are present.
- ***TestCases:*** All test methods present in this package.
- ***TestData:*** Location of Excel file.
- ***Utility:***  config file and Excel reader file present.

####PageObject files description
+ ***LoginPage:*** All locators and Action methods are available of login page
+ ***SignUpPage:*** All signup locators and Action Method are available.
+ ***NewAddressPage:*** All locators and Action methods are available of new address page 
+ ***SearchPage:*** All locators and Action methods are available of search page
+ ***Delete:*** All locators and Action methods are available of delete page

####TestCases files description
+ ***LoginTest:*** All locators and Action methods are available of login test
+ ***SignUpTest:*** All signup test locators and Action Method are available.
+ ***NewAddressTest:*** All locators and Action methods are available of new address test 
+ ***SearchTest:*** All locators and Action methods are available of search test
+ ***DeleteTest:*** All locators and Action methods are available of delete test
+ ***conftest:*** Browser setup present here.

####Other file description
+ ***config:*** some basic data store in this file.
+ ***ExcelDataReader:*** Excel data retrieving code 
+ ***drivers:*** All drivers file available here.

####Dependency
+ Every successful Sign Up shall change the email of the Excel file