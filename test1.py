import unittest

def sum(a, b):
    return a + b

class SumTest(unittest.TestCase):
    
    def setUp(self):
        print("SETUP Called...")
        self.a = 10
        self.b = 20
        
    def tearDown(self):
        self.a = 0
        self.b = 0
        print("TEARDOWN Called...")
    
    def test_sumfunc_1(self):
        print("TEST - 1 Called...")
        # # Arrange
        # a = 10
        # b = 20
        # Act
        result = sum(self.a, self.b)
        # Assert
        self.assertEqual(result, self.a + self.b)
        
    def test_sumfunc_2(self):
        print("TEST - 2 Called...")
        # Arrange
        # a = 10
        # b = 20
        # Act
        result = sum(self.b, self.a)
        # Assert
        self.assertEqual(result, self.a + self.b)

# class LearnTest(unittest.TestCase):
    
#     # def test_myfunc(self):
#     #     pass
    
#     # def test_func_1(self):
#     #     pass
    
#     def test_func_2(self):
#         pass
    
# class AnotherTest(unittest.TestCase):
    
#     def test_func_2(self):
#         pass


if __name__ == '__main__':
    unittest.main()
    
    