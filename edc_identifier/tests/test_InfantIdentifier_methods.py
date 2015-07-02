from django.test import TestCase
from django.db import models
#from edc_base.model.models import BaseUuidModel
from ..exceptions import IdentifierError


from ..classes import InfantIdentifier,SubjectIdentifier
#from ..classes import SubjectIdentifier
from ..models import BaseIdentifierModel

class StudySite(models.Model):
    
    class Meta:
        app_label = 'edc_identifier'

    
    site_code = models.CharField(max_length=4, unique=True)

    site_name = models.CharField(max_length=35, unique=True)
 
class InfantIdentifierModel(BaseIdentifierModel): 
    
    objects = models.Manager()

    class Meta:
        app_label = 'edc_identifier'
        ordering = ['-created']
        
   
    
class TestInfantIdentifierMethods(TestCase):
    
    def setUp(self):
        
        model_name='subjectIdentifier'
        app_label='edc_identifier'
        study_site=StudySite(site_code='56', site_name='Mogoditshane')
        site_code='56'
        is_derived=False
        add_check_digit=False
        
        live_infants=2
        birth_order=1
        
        self.identifier=SubjectIdentifier(app_name='edc_identifier',model_name='subjectIdentifier',identifier_prefix='056',site_code=site_code, 
                                          is_derived=is_derived,add_check_digit=add_check_digit,padding=4)
        self.identifier.modulus=7
         
        self.instance=InfantIdentifier(model_name=model_name, app_name=app_label,maternal_identifier=self.identifier.get_identifier(add_check_digit=True),study_site=study_site,
                                       live_infants=live_infants,live_infants_to_register=2,birth_order=birth_order) 
              
                              
    def test_get_base_suffix(self):
        """asserts that the base suffix is calculated properly"""   
        self.assertEqual(self.instance._get_base_suffix(),25)
        
    
    def test_get_suffix(self):
        """asserts that the suffix is calculated properly""" 
        self.assertEqual(self.instance._get_suffix(),35)
        
    def test_get_identifier_prep(self):
        self.assertEqual(self.instance.get_identifier_prep(),{'suffix': 35, 'maternal_identifier': '056-56991001-4'})
        
    def test_get_identifier_prep1(self):    
        """asserts suffix is calculated properly with diff number of infants""" 
        self.instance.live_infants=3 
        self.assertEqual(self.instance.get_identifier_prep(),{'suffix': 46, 'maternal_identifier': '056-56991001-4'})
        
    def test_get_identifier_prep2(self): 
        "asserts that an exception gets raised if maternal identifier doesn't exist in the subjectIdentifier"
        self.instance.maternal_identifier='066-99561001-1'
        self.assertRaises(IdentifierError,self.instance.get_identifier_prep)
        
    def test_get_identifier_prep3(self):
        "asserts that an exception gets raised if number of live_infants is less than one"
        self.instance.live_infants=0
        self.assertRaises(IdentifierError,self.instance.get_identifier_prep)
         
             
        
             
    #def test_get_identifier_post(self):
        #"""asserts that an update is made after creating a new-identifier"""
        #print(self.instance.get_identifier_post(self.identifier.get_identifier(add_check_digit=True)))     