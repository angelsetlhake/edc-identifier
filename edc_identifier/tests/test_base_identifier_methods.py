from django.test import TestCase

#from ..classes import Identifier
#from ..classes import CheckDigit
from ..classes import BaseIdentifier,SubjectIdentifier
#from ..exceptions import CheckDigitError, IdentifierEncodingError, IdentifierDecodingError

#from ..models import SubjectIdentifier

from ..models import BaseIdentifierModel

class  TestModel(BaseIdentifier):
       
    class Meta:
            app_label = 'edc_identifier'
     
            
class TestModelTestCase(TestCase):

    def setUp(self):
        site_code='10'
        is_derived=True
        add_check_digit=None
        padding=4
        is_derived=False
        
          
        #TestModel.objects.all().delete()
        
        self.instance = SubjectIdentifier(app_name='edc_identifier', model_name='sequence', site_code= site_code,
                        add_check_digit=add_check_digit,padding=padding,is_derived=is_derived)
        self.instance._set_sequence_model_name('identifier')  
        self.instance._set_sequence_app_label('edc_identifier')
        
        self.assertEqual(self.instance.is_derived,False)
        
       
       
    def test_sequence_model_name(self):
       
        self.assertEqual(self.instance._get_sequence_model_name(),'identifier')
        
    def test_sequence_app_label(self):  
        self.assertEqual(self.instance._get_sequence_app_label(),'edc_identifier')
        
        self.assertEqual(self.instance.get_identifier_prep(),{})
        
          
    def test_get_identifier_prep(self):    
        
        self.assertEqual(self.instance.get_identifier_prep(),{})
        
    def test_get_identifier_history_model_options(self):
        self.assertTrue(self.instance._get_identifier_history_model_options())
       
       
            
       
       

       
            
        
        
        
        
    
        
        
        
        
   
           

     
         
    
    
     