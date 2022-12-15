import unittest
from unittest.mock import MagicMock
from inventory_client import InventoryClient
from get_book_titles import get_book_titles

class Client_Tests(unittest.TestCase):
    def test01(self):
        InventoryClientMock = InventoryClient()
        InventoryClientMock.getBookTitles = MagicMock(return_value = ["Happy Coding", "Take Photos"])
        InventoryClientMock.getBookTitles(["1", "2"], key = "value")
        res = get_book_titles(InventoryClientMock, ["1", "2"])
        exp = ["Happy Coding", "Take Photos"]
        self.assertEqual(res, exp)
    def test02(self):
        InventoryClientReal = InventoryClient()
        res = get_book_titles(InventoryClientReal, ["1", "2"])
        exp = ["Happy Coding", "Take Photos"]
        self.assertEqual(res, exp)
        
if __name__ == '__main__':
    unittest.main()