from email.mime import application
from urllib import response
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Application, Configuration

class MCCTestCase(APITestCase):
    """
    Mission Control Center Unit test handler.
    
    """
    
    def setUp(self):
        self.application_1 = Application.objects.create(
            name='app_name_test_1', 
            department='app_department_test_1', 
            description='app_description_test_1')

        self.application_2 = Application.objects.create(
            name='app_name_test_2', 
            department='app_department_test_2', 
            description='app_description_test_2')

        self.configuration_1 = Configuration.objects.create(
            type_choice='meta',
            roles_set={'app_name_role': 'name role', 'app_code': 'app value'},
            application=self.application_1)

        self.configuration_2 = Configuration.objects.create(
            type_choice='meta',
            roles_set={'app_name_role': 'name role', 'app_code': 'app value'},
            application=self.application_2)

    def test_get_applications_list_200(self):
        response = self.client.get(
            '/api/v1/applications/', format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(type(response.json()), list)
        
        json_response = response.json()
        self.assertEqual(2, len(json_response))

    def test_get_configuration_list_200(self):
        response = self.client.get(
            '/api/v1/configurations/', format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(type(response.json()), list)
        
        json_response = response.json()
        self.assertEqual(2, len(json_response))

        response = self.client.get(
            '/api/v1/configurations/', 
            {'application': self.application_1.pk}, 
            format='json'
        )
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(type(response.json()), list)

        json_response = response.json()
        self.assertEqual(1, len(json_response))

    def test_get_configuration_list_400(self):
        response = self.client.get(
            '/api/v1/configurations/', 
            {'application': 9}, 
            format='json'
        )
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_configuration_list_404(self):
        response = self.client.get(
            '/api/v1/configurations/', 
            {'application': "adsa"}, 
            format='json'
        )
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_configuration_201(self):
        response = self.client.post(
            '/api/v1/configurations/',
            {
                'type_choice': 'tech', 'roles_set': {
                    'app_name_v1': 'app name v1', 
                    'app_code_v1': 'app code v1'
                },
                'application': self.application_1.pk
            },
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(type(response.json()), dict)

    def test_update_configuration_200(self):
        response = self.client.put(
            '/api/v1/configurations/{conf_pk}/'.format(
                conf_pk=self.configuration_1.pk),
            {
                'type_choice': self.configuration_1.type_choice,
                'application': self.configuration_1.application.pk,
                'roles_set': {
                    'app_name_v2': 'app name v2', 
                    'app_code_v2': 'app code v2'
                },
            },
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(type(response.json()), dict)

    def test_get_version_list_200(self):
        response = self.client.put(
            '/api/v1/configurations/{conf_pk}/'.format(
                conf_pk=self.configuration_2.pk),
            {
                'type_choice': self.configuration_2.type_choice,
                'application': self.configuration_2.application.pk,
                'roles_set': {
                    'app_name_v2': 'app name v2', 
                    'app_code_v2': 'app code v2'
                },
            },
            format='json'
        )

        response = self.client.put(
            '/api/v1/configurations/{conf_pk}/'.format(
                conf_pk=self.configuration_2.pk),
            {
                'type_choice': self.configuration_2.type_choice,
                'application': self.configuration_2.application.pk,
                'roles_set': {
                    'app_name_v3': 'app name v3', 
                    'app_code_v3': 'app code v3'
                },
            },
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(type(response.json()), dict)

        response = self.client.get(
            '/api/v1/configurations/{conf_pk}/versions/'.format(
                conf_pk=self.configuration_2.pk)
        )
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(type(response.json()), list)

        json_response = response.json()
        self.assertEqual(2, len(json_response))

    def test_get_version_list_400(self):
        response = self.client.get(
            '/api/v1/configurations/{conf_pk}/versions/'.format(
                conf_pk="fsadfas")
        )
        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_get_version_list_404(self):
        response = self.client.get(
            '/api/v1/configurations/{conf_pk}/versions/'.format(
                conf_pk=1000000)
        )
        
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
            