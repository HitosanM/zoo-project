import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def test_child_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(-1), "Your age can’t less than 0")
        self.assertEqual(self.zoo.get_ticket_price(8), 50)
        self.assertEqual(self.zoo.get_ticket_price(18), 100)
        self.assertEqual(self.zoo.get_ticket_price(40), 150)
        self.assertEqual(self.zoo.get_ticket_price(100), 100)
       
    # Add your additional test cases here.


if __name__ == '__main__':
    unittest.main()