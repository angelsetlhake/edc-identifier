from django.test import TestCase

from ..classes import CheckDigit
from ..exceptions import CheckDigitError, IdentifierEncodingError, IdentifierDecodingError


class CheckDigitMethodsTests(TestCase):

    def test_modulus_greater_than_ten(self):
        number=85749-3-283
        modulus=11
        checkDigit=number%modulus
        self.assertEqual(CheckDigit.calculate(number,modulus),checkDigit)
         

    def test_check_num_correct_input(self):
        number=4593
        modulus=10
        checkDigit=number%modulus
        self.assertEqual(CheckDigit.calculate(number,modulus),checkDigit)  

    def test_modulus_greater_than_100(self):
        number=1237-93-876912
        modulus=102
        checkDigit=number%modulus
        self.assertTrue(CheckDigit.calculate(number,modulus),checkDigit)
        
    
    def test_modulus_zero(self):    
        number=7469-2-3456
        modulus=0
        self.assertRaisesRegexp(ValueError,"cannot divide by 0")  
   
         
    def test_invalid_input(self):
        number='9785637291 '
        modulus=7
        self.assertRaisesRegexp(ValueError,"number cannot be a string")    
        
        
     
    def test_check_num_wrong_input(self):
    
        number=1237
        modulus=102
        checkDigit=number%modulus
        self.assertNotEqual(CheckDigit.calculate(number,modulus),checkDigit)
            
             
      
                  
                  
    