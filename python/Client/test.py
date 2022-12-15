import unittest
from unittest.mock import MagicMock
from inventory_client import InventoryClient
from get_book_titles import get_book_titles

class Client_Tests(unittest.TestCase):
    '''
    Test using mock client
    '''
    def test01(self):
        print("Test1: Using Mock Client\n")
        InventoryClientMock = InventoryClient()
        InventoryClientMock.getBookTitles = MagicMock(return_value = ["Happy Coding", "Take Photos"])
        InventoryClientMock.getBookTitles(["1", "2"], key = "value")
        res = get_book_titles(InventoryClientMock, ["1", "2"])
        exp = ["Happy Coding", "Take Photos"]
        self.assertEqual(res, exp)
    '''
    Test using real server
    '''
    def test02(self):
        print("\n")
        print("Test2: Using Real Server\n")
        try:
            InventoryClientReal = InventoryClient()
            res = get_book_titles(InventoryClientReal, ["1", "2"])
            exp = ["Happy Coding", "Take Photos"]
            self.assertEqual(res, exp)
        except:
            print("Server Not Started\n")
        
if __name__ == '__main__':
    unittest.main()