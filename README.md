## Acceptance testing framework for e-commerce project<br>
**The essence of this project is to create a structure that is suitable for writing tests for any e-commerce project.**<br>
This project is an example of constructing the acceptance testing framework for the site http://automationpractice.com/index.php

The directory tree:

```bash
├── actions
│   ├── __init__.py
│   ├── actions.py
│   └── test_data.py
├── checkout
│   ├── __init__.py
│   ├── case_checkout_registration.py
│   └── suite_checkout.py
├── README.md
├── runner.py

```
<hr>
Directory actions:<br> 
This directory acts as a kernel, which contains the necessary data for testing and ready-made methods that
can be used in various test-cases without repeating.<br>
This will help to easily debug and refine the test-case by following the DRY principle.<br>
<br>
actions.py - contains methods that can be used many times in different test cases.<br>
test_data.py - contains test data of the project (personal info, address etc.).


<hr>
Directory checkout:<br>
This directory is a separate unit that contains everything that concerns the checkout part of the project.<br>
In this directory, you need to create test cases that refer only to checkout and combine them into test-suites in suite_checkout.py file.
<br>
<br>
suite_checkout.py - this file is a test-suite that combines all the test cases related to the checkout.
This makes it convenient to import and run tests separately for any test-suite.
<br>
case_checkout_registration.py - this is a sample test case that uses the methods described in actions.py that can be reused
 or added to the test case itself without changing them so as not to damage other test cases that can use these methods.
<br>
<hr>


 

