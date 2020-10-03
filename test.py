import unittest 
from main import MyClass

class SimpleTest(unittest.TestCase): 
  
    # Returns True or False.  
    def test(self):            
        val = MyClass().myMethod() 
        self.assertTrue(val) 

if __name__ == '__main__': 
    unittest.main() 