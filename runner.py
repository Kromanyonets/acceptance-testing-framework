import unittest
import sys

from checkout.suite_checkout import checkout_test_suite

unittest.TextTestRunner(verbosity=2).run(checkout_test_suite)

