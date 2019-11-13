import unittest


class MyTestCase(unittest.TestCase):

    def setUp(self):
        # the fixture .....
        print("Setting up.....")

    def test_employee(self):
        assert 1 == 1

    def tearDown(self):
        print("Tear Down")


if __name__ == "__main__":
    unittest.main()
