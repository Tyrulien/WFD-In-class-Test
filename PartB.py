# PartB.py
# This file contains unit tests for the classes defined in PartA.py.
import unittest
from PartA import Phone, Smartphone

class TestInstanceChecks(unittest.TestCase):
    def setUp(self):
        # Create instances for testing
        self.phone = Phone("Nokia", "3310", 2000, 49.99, "Blue")
        self.smartphone = Smartphone("Google", "Pixel 6", 2021, 599.99, "Black", "Android", 128)
    
    def test_instance_of_phone(self):
        # Test that phone is an instance of Phone
        self.assertIsInstance(self.phone, Phone)
    
    def test_not_instance_of_smartphone(self):
        # Test that phone is NOT an instance of Smartphone
        self.assertNotIsInstance(self.phone, Smartphone)
    
    def test_instances_identical(self):
        # Create two variables referencing the same object
        phone_alias = self.phone
        self.assertIs(self.phone, phone_alias)

class TestUpdateMethods(unittest.TestCase):
    def setUp(self):
        self.phone = Phone("LG", "G6", 2017, 299.99, "Silver")
        self.smartphone = Smartphone("OnePlus", "9", 2021, 729.99, "Red", "Android", 128)

    def test_update_phone_attributes(self):
        # Test updating phone attributes works correctly
        self.phone.update_brand("LG Electronics")
        self.phone.update_model("G6 Plus")
        self.phone.update_year(2018)
        self.phone.update_price(349.99)
        self.phone.update_colour("Gray")
        
        self.assertEqual(self.phone.brand, "LG Electronics")
        self.assertEqual(self.phone.model, "G6 Plus")
        self.assertEqual(self.phone.year, 2018)
        self.assertEqual(self.phone.price, 349.99)
        self.assertEqual(self.phone.colour, "Gray")
    
    def test_update_smartphone_extra_attributes(self):
        # Test updating extra attributes in Smartphone
        self.smartphone.update_operating_system("Android 12")
        self.smartphone.update_storage_capacity(256)
        
        self.assertEqual(self.smartphone.operating_system, "Android 12")
        self.assertEqual(self.smartphone.storage_capacity, 256)

def main():
    # Run all the unit tests
    suite = unittest.TestLoader().loadTestsFromTestCase(TestInstanceChecks)
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestUpdateMethods))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

if __name__ == '__main__':
    main()
