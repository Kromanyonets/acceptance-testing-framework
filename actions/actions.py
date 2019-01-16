import requests

from . import test_data
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select



class CommonActions(object):
    """
     This class contains methods that are often used in various test cases.
     This approach will make it easier to maintain and edit tests as needed.

    """
    def start(self):
        """
        Methods with preconditions.
        Here we can start browser session and give it some custom options.
        :return:
        """
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def stop(self):
        """
        Closed browser session and end the test.
        :return:
        """
        self.driver.quit()

    def check_page_status(self, page_url=None):
        """
        Method which can check page response status.
        :param page_url:
        :return:
        """
        r = requests.get(page_url)
        print(r.status_code)

    def go_home_page(self):
        """
        Simple methods which redirect to Home Page.
        :return:
        """
        self.driver.get(test_data.home_page)

    def add_product_and_go_to_the_cart(self):
        """
        Going to test product page.
        Adding that product to the cart and checking if it is OK.
        If ok - we are redirected to the Cart page.
        :return:
        """
        self.driver.get(test_data.product_page)
        self.driver.find_element_by_xpath("//span[contains(text(),'Add to cart')]").click()
        assert ('Product successfully added to your shopping cart' in self.driver.page_source)
        WebDriverWait(self.driver, 4).until(
            EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Proceed to checkout')]"))
        ).click()

    def go_to_sign_in_step(self):
        """
        Checking if we are on Cart page.
        After checking going to Step 2 checkout.
        :return:
        """
        assert ('Shopping-cart summary' in self.driver.page_source)
        WebDriverWait(self.driver, 4).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "standard-checkout"))
        ).click()

    def reg_on_checkout(self):
        """
        Choose registration on checkout input,
        fill in email and click submit to go to registration field.
        :return:
        """
        email_reg = WebDriverWait(self.driver, 4).until(
            EC.visibility_of_element_located((By.ID, "email_create"))
        )
        email_reg.send_keys(test_data.email)
        self.driver.find_element_by_id('SubmitCreate').click()

    def fill_in_personal_info(self):
        """
        Fill in all necessary personal information.
        :return:
        """
        WebDriverWait(self.driver, 4).until(
            EC.visibility_of_element_located((By.ID, "id_gender1"))
        ).click()
        self.driver.find_element_by_id('customer_firstname').send_keys(test_data.name)
        self.driver.find_element_by_id('customer_lastname').send_keys(test_data.surname)
        self.driver.find_element_by_id('passwd').send_keys(test_data.password)

    def fill_in_address_info(self):
        """
        Fill in all necessary address information.
        :return:
        """
        self.driver.find_element_by_id('firstname').send_keys(test_data.name)
        self.driver.find_element_by_id('lastname').send_keys(test_data.surname)
        self.driver.find_element_by_id('address1').send_keys(test_data.address)
        self.driver.find_element_by_id('city').send_keys(test_data.city)
        self.driver.find_element_by_id('postcode').send_keys(test_data.zip)
        self.driver.find_element_by_id('phone_mobile').send_keys(test_data.mobile_phone)
        self.driver.find_element_by_id('alias').send_keys(test_data.alias)

        # Choose first state from list
        state_selector = Select(self.driver.find_element_by_id('id_state'))
        state_selector.select_by_visible_text('Alabama')

    def submit_registration(self):
        """
        Submit registration on checkout or registration page.
        :return:
        """
        self.driver.find_element_by_id('submitAccount').click()
