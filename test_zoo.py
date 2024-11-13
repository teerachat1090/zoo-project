import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def test_no_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(-1), 0)

    def test_child_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(0), 50)

    def test_teen_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(20), 100)

    def test_adult_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(60), 150)

    def test_old_people_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(61), 100)

if __name__ == '__main__':
    unittest.main()