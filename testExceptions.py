import unittest
    
def throw_ex(var):
    if var == 100:
        raise Exception("NOT A VALID NUMBER")
    else:
        return True
        
class LearnTest(unittest.TestCase):
    
    def test_sample(self):
        self.assertEqual(throw_ex(10), True)
    
if __name__ == '__main__':
    unittest.main()