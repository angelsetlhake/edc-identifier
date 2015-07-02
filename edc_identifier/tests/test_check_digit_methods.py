from django.test import TestCase

from ..classes import CheckDigit
<<<<<<< HEAD



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
        
=======
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
        
    
>>>>>>> 17cdb2dfd138288c50c8d002a1bb0a8523a2786b
    def test_modulus_zero(self):    
        number=7469-2-3456
        modulus=0
        self.assertRaisesRegexp(ValueError,"cannot divide by 0")  
   
         
    def test_invalid_input(self):
<<<<<<< HEAD
        "asserts that an exception is raised if number given is a string"
        number='9785637291 '
        modulus=7
        self.assertRaisesRegexp(ValueError,"number cannot be a string")  
     
    def test_check_num_wrong_input(self):
=======
        number='9785637291 '
        modulus=7
        self.assertRaisesRegexp(ValueError,"number cannot be a string")    
        
        
     
    def test_check_num_wrong_input(self):
    
>>>>>>> 17cdb2dfd138288c50c8d002a1bb0a8523a2786b
        number=1237
        modulus=102
        checkDigit=number%modulus
        self.assertNotEqual(CheckDigit.calculate(number,modulus),checkDigit)
            
             
      
                  
<<<<<<< HEAD
=======
                  
>>>>>>> 17cdb2dfd138288c50c8d002a1bb0a8523a2786b
    