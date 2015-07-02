from django.test import TestCase

from ..classes import InfantIdentifier,Identifier,BaseIdentifier
from edc.core.bhp_variables.models import StudySite

class  TestModel(InfantIdentifier):
       
    class Meta:
            app_label = 'edc_identifier'
     



class TestInfantIdentifierMethods(TestCase):
      
      def setUp(self):
          maternal_identifier='056-19800001-3'
          site_code='10'
          live_infants='2'
          birth_order=None
          
          TestModel.objects.all().create()
          
          self.instance=Studysite(study_code='10',study_name='Mogoditshane')
          
          self.instance=InfantIdentifier(maternal_identifier=maternal_identifier,study_site=site_code,
                                          live_infants=live_infants,live_infants_to_register=2,birth_order=birth_order)  
                              
                              
      def test_get_base_suffix(self):
          
          self.assertEqual(self.instance._get_identifier_suffix(),25) 
          
      def test_get_identifier_post(self):
          self.martenalid='056-19800001-2'
          self.assertEqual(self.instance.get_identifier_post('056-19800001-2'),martenalid)
       
              
          
          
