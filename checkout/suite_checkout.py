import unittest

from .case_checkout_registration import CheckoutRegistrationTestCase
"""
In this module, we load test cases from each module separately and combine them into a test-suite.

"""
# Example of loading a test-case which will be transmitted to the test-suite.
checkout_registration_test = unittest.TestLoader().loadTestsFromTestCase(CheckoutRegistrationTestCase)

# Here all test-cases relating to the guest checkout are combined in to one test suite.
checkout_test_suite = unittest.TestSuite([checkout_registration_test])