import os
import sys
import unittest

from empty import Empty  # noqa
from empty import app_factory  # noqa

from test_empty.test_commands import TestRoute
from test_empty.test_filters import TestFilters
from test_empty.test_app import TestEmpty

CURR_DIR = os.path.abspath('.')
sys.path.insert(0, os.path.join(CURR_DIR, 'test_empty/apps'))


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestRoute))
    suite.addTest(unittest.makeSuite(TestFilters))
    suite.addTest(unittest.makeSuite(TestEmpty))
    return suite


if __name__ == '__main__':
    unittest.main(defaultTest='suite')
