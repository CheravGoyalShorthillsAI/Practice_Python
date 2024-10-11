import unittest
import buy_and_sell_stock

class TestMaxProfit(unittest.TestCase):
    def test_max_profit(self):
        self.assertEqual(buy_and_sell_stock.max_profit([7,1,5,3,6,4]), 5)
        self.assertEqual(buy_and_sell_stock.max_profit([7,6,4,3,1]), 0)
        self.assertEqual(buy_and_sell_stock.max_profit([1,2,3,4,5]), 4)
        self.assertEqual(buy_and_sell_stock.max_profit([2,4,1]), 2)
        self.assertEqual(buy_and_sell_stock.max_profit([3,3,5,0,0,3,1,4]), 4)

if __name__ == "__main__":
    unittest.main()
