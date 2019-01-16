import unittest

from actions.actions import CommonActions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutRegistrationTestCase(unittest.TestCase, CommonActions):
    """
     This class is an example of a step-by-step test case.
     Here, we use the methods described in the actions.py module

    Also this class containt all test-case steps:
    1. Start browser.
    2. Add test-product and go to the cart.
    3. Go to second step of checkout.
    4. Choose registration on checkout.
    5. Fill in all necessary personal info.
    6. Fill in all necessary address info.
    7. Submit registration.
    ::return
    """
    def setUp(self):
        # Start browser.
        self.driver = webdriver.Chrome() # We can write unique preconditions, but for correct compatibility
        self.driver.maximize_window()    # use self.driver when creating browser instance (not self.test_driver, or something else).

    def test_checkout_registration(self):
        # Add test-product and go to the cart.
        CommonActions.add_product_and_go_to_the_cart(self)

        # Go to second step of checkout.
        CommonActions.go_to_sign_in_step(self)

        # This is same as go_to_sign_in_step methods which is described above, and it will work correctly.
        # So you can change, modify or do what your test-case require.
        #
        # assert ('Shopping-cart summary' in self.driver.page_source)
        # WebDriverWait(self.driver, 4).until(
        #     EC.visibility_of_element_located((By.CLASS_NAME, "standard-checkout"))
        # ).click()
        #

        # Choose registration on checkout.
        CommonActions.reg_on_checkout(self)

        # Fill in all necessary personal info.
        CommonActions.fill_in_personal_info(self)

        # Fill in all necessary address info.
        CommonActions.fill_in_address_info(self)

        # Submit registration.
        CommonActions.submit_registration(self)

    def tearDown(self):
        CommonActions.stop(self)