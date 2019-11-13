
import unittest


class SampleTestCase(unittest.TestCase):
    def setUp(self):
        print("setup init")
        self.a = 10

    def test_1(self):
        print("testing")

    def tearDown(self):
        print("setup init")
        self.a = 0


def test_login():
    assert 1 == 1


@unittest.skip("To Skip")
def test_logout():
    assert 1 == 1


def suite():
    suite = unittest.TestSuite()
    suite.addTest(SampleTestCase('test_1'))


