import unittest
from invoice_calculator import divide_pay

class InvoiceCalculatorTests(unittest.TestCase):
    def test_divided_fairly(self):
        self.assertEqual(divide_pay(360.0, {"Alice": 3.0, "Bob": 3.0, "Carol": 6.0}),{"Alice": 90, "Bob": 90, "Carol": 180})
         
if __name__ == "__main__":
    unittest.main()