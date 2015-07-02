from django.test import TestCase

from ..classes import CheckDigit


class CheckDigitMethodsTests(TestCase):
    
    def setUp(self):
        
        number="056-5699-1"
        
        def get_num(x):
           
            return int(''.join(ele for ele in x if ele.isdigit()))
        
       
        self.instance=get_num(number)
        
    
    def test_modulus_greater_than_ten(self):
        "asserts that check_digit is calculated properly,using modulus greater than ten"
        modulus=11
        checkDigit=self.instance%modulus
        self.assertEqual(CheckDigit.calculate(self,number=self.instance,modulus=modulus),checkDigit)
        
    def test_modulus_equal_ten(self):
        "asserts that check_digit is calculated properly,using modulus equal to ten"
        modulus=10
        checkDigit=self.instance%modulus
        self.assertEqual(CheckDigit.calculate(self,number=self.instance,modulus=modulus),checkDigit)  

    def test_modulus_greater_than_100(self):
        "asserts that the format for check_digit is correct"
        modulus=102
        checkDigit=self.instance%modulus
        self.assertEqual(CheckDigit.calculate(self,number=self.instance,modulus=modulus),'071')
        
    def test_modulus_zero(self):    
        number=7469-2-3456
        modulus=0
        self.assertRaisesRegexp(ValueError,"cannot divide by 0")  
   
    def test_invalid_input(self):
        "asserts that an exception is raised if number given is a string"
        number='9785637291 '
        modulus=7
        self.assertRaisesRegexp(ValueError,"number cannot be a string")  
    
    
