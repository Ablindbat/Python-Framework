### Automation of automationpractice.com site
<br> site [link](http://automationpractice.com/index.php)
<br>
+ For Single file run in terminal command is:</br>
 ``pytest -s -v "filename with extention"``
+ For while tests are run in terminal command ia: </br>
``pytest -s -v``
+ Run mark file:</br>
``pytest -m "marker name" "file name"``


#### Package description
- ***[PageObject](https://github.com/Rajib8016/Python-Framework/tree/master/PageObject):*** All pages are available in this package and all locator and methods are present.
- ***[TestCases](https://github.com/Rajib8016/Python-Framework/tree/master/TestCases):*** All test methods present in this package.
- ***[TestData](https://github.com/Rajib8016/Python-Framework/tree/master/TestData):*** Location of Excel file.
- ***[Utility](https://github.com/Rajib8016/Python-Framework/tree/master/utility):***  config file and Excel reader file present.

#### PageObject files description
+ ***[LoginPage](https://github.com/Rajib8016/Python-Framework/blob/master/PageObject/LoginPage.py):*** All locators and Action methods are available of login page
+ ***[SignUpPage](https://github.com/Rajib8016/Python-Framework/blob/master/PageObject/SignUpPage.py):*** All signup locators and Action Method are available.
+ ***[NewAddressPage](https://github.com/Rajib8016/Python-Framework/blob/master/PageObject/NewAddressPage.py):*** All locators and Action methods are available of new address page 
+ ***[SearchPage](https://github.com/Rajib8016/Python-Framework/blob/master/PageObject/SearchPage.py):*** All locators and Action methods are available of search page
+ ***[Delete](https://github.com/Rajib8016/Python-Framework/blob/master/PageObject/DeletePage.py):*** All locators and Action methods are available of delete page

#### TestCases files description
+ ***[LoginTest](https://github.com/Rajib8016/Python-Framework/blob/master/TestCases/test_LoginTest.py):*** All locators and Action methods are available of login test
+ ***[SignUpTest](https://github.com/Rajib8016/Python-Framework/blob/master/TestCases/test_SignupTest.py):*** All signup test locators and Action Method are available.
+ ***[NewAddressTest](https://github.com/Rajib8016/Python-Framework/blob/master/TestCases/test_NewAddressTest.py):*** All locators and Action methods are available of new address test 
+ ***[SearchTest](https://github.com/Rajib8016/Python-Framework/blob/master/TestCases/test_SearchTest.py):*** All locators and Action methods are available of search test
+ ***[DeleteTest](https://github.com/Rajib8016/Python-Framework/blob/master/TestCases/test_DeleteTest.py):*** All locators and Action methods are available of delete test
+ ***[conftest](https://github.com/Rajib8016/Python-Framework/blob/master/TestCases/conftest.py):*** Browser setup present here.

#### Other file description
+ ***[config](https://github.com/Rajib8016/Python-Framework/blob/master/utility/config.py):*** some basic data store in this file.
+ ***[ExcelDataReader](https://github.com/Rajib8016/Python-Framework/blob/master/utility/ExcelDataReader.py):*** Excel data retrieving code 
+ ***[drivers](https://github.com/Rajib8016/Python-Framework/tree/master/drivers):*** All drivers file available here.

#### Dependency
+ Every successful Sign Up shall change the email of the Excel file
