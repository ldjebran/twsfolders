#!/usr/bin/env python

import unittest


def all_tests():
    test_loader = unittest.TestLoader()
    return test_loader.loadTestsFromNames(['twsfolders.tests.test_rootfolders',
                                           'twsfolders.tests.test_folder'
                                           ]
                                          )


if __name__ == '__main__':
    suite = all_tests()
    unittest.TextTestRunner(verbosity=2).run(suite)
