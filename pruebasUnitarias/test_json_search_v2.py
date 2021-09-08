# Fill the Python code in this file
import unittest
from recursive_json_search_v2 import *
from test_data import *
class Json_Search_Test(unittest.TestCase):
    "Modulo de prueba para probar la función de busqueda en  recursive_json_search.py"

    def test_search_found(self):

        self.assertTrue([] !=json_search(key1,data))
    
    def test_search_not_found(self):
        self.assertTrue([] == json_search(key2,data))
    
    def test_is_a_list(self):
        self.assertIsInstance(json_search(key1,data), list)

if __name__ =='__main__':
     unittest.main()  