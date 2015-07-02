from django.test import TestCase

from ..classes import SubjectIdentifier

from ..models import BaseIdentifierModel
from ..exceptions import IdentifierError

class  TestModel(BaseIdentifierModel):
       
    class Meta:
            app_label = 'edc_identifier'
           
     
            
class TestModelTestCase(TestCase):

    def setUp(self):
        site_code='10'
        add_check_digit=False
        padding=4
        is_derived=False
        
        
        
        
        self.instance = SubjectIdentifier(app_name='edc_identifier', model_name='subjectIdentifier', site_code= site_code,
                        add_check_digit=add_check_digit,is_derived=is_derived,identifier_prefix='066',padding=padding)
        self.instance.modulus=7
        self.instance.sequence_number=1001
        
        self.instance._set_sequence_model_name('identifier')  
        
        self.instance._set_sequence_app_label('edc-identifier')
        
       
    def test_sequence_model_name(self):
        self.assertEqual(self.instance._get_sequence_model_name(),'identifier')
        
    def test_sequence_app_label(self):  
        self.assertEqual(self.instance._get_sequence_app_label(),'edc-identifier')
           
        
        self.assertEqual(self.instance.get_identifier_prep(),{})
        
    def test_get_identifier_history_model_options(self):
        self.assertTrue(self.instance._get_identifier_history_model_options())
        
    def test_get_identifier_prep(self):
        identifier_prep= {'site_code': '10', 'identifier_prefix': '066', 'device_id': '99'}
        self.assertEqual(self.instance._get_identifier_prep(),identifier_prep) 
        
    def test_get_identifier(self):
        
        "asserts that an exception is raised when Instance attribute is_derived has not been set"
        self.instance.is_derived=None
        self.assertRaises(AttributeError,self.instance.get_identifier)
        
    def test_get_identifier1(self):    
        "asserts that an exception is raised if check_digit is not set or its equal to None" 
        self.instance.add_check_digit=None
        self.assertRaises(AttributeError,self.instance.get_identifier )
        
    def test_get_identifier2(self):
        "asserts that check_digit is added"
        self.assertEqual(self.instance.get_identifier(add_check_digit=True),'066-10991001-6')
        
    def test_get_identifier3(self):
        "asserts that check_digit is not added"
        self.assertEqual(self.instance.get_identifier(add_check_digit=False),'066-10991001')    
        
          
        
  
    
            
     
        
       
        
        
       
         
   
            
   
       
    