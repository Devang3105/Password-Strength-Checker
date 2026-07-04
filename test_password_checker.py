import unittest
from password_checker import check_password

class TestPasswordChecker(unittest.TestCase):
    def test_weak_password(self):
        result = check_password("123456")
        self.assertEqual(result["Strength"], "Weak")

    def test_medium_password(self):
        result = check_password("Password123")
        self.assertEqual(result["Strength"], "Medium")
        self.assertEqual(result["Score"], 4)

    def test_strong_password(self):
        result = check_password("Hello123@")
        self.assertEqual(result["Strength"], "Strong")
        self.assertEqual(result["Score"], 5)
        self.assertEqual(len(result["Suggestions"]), 0) 
        
    def test_numbers_only(self):
        result = check_password("1234567890")
        self.assertEqual(result["Strength"], "Weak")
        
        
    def test_uppercase_only(self):
        result = check_password("PASSWORD")
        self.assertEqual(result["Strength"], "Weak")
        
        
    def test_lowercase_only(self):
        result = check_password("password")
        self.assertEqual(result["Strength"], "Weak")
        
        

if __name__ == "__main__":
    unittest.main()