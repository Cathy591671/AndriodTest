# -*- coding: utf-8 -*-
import unittest
class zcj(unittest.TestCase):

    def setUp(self):
        print "setUp"

    def test_swipe(self):
        print "Swipe"

    def test_login(self):
        print "login"

    def tearDown(self):
        print 'tearDown'

if __name__ == '__main__':
    unittest.main()
    '''
    testsuite=unittest.TestSuite()

    testsuite.addTest(zcj("test_swipe"))
    testsuite.addTest(zcj("test_login"))

    runner=unittest.TextTestRunner()


    runner.run(testsuite)
    print "run被执行了"
'''
