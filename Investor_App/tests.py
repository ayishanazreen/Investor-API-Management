from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
import json

class InvestorTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        # Add JWT token to client header if using authentication

    def test_create_investor(self):
        response = self.client.post('/api/investor/', {
            'name': 'John Doe',
            'email': 'john@example.com',
            'phone': '1234567890'
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_investors(self):
        response = self.client.get('/api/investors/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check if the list is correct

    def test_delete_investor(self):
        self.client.post('/api/investor/', {
            'name': 'John Doe',
            'email': 'john@example.com',
            'phone': '1234567890'
        }, format='json')
        response = self.client.delete('/api/investor/john@example.com/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_update_investor(self):
        self.client.post('/api/investor/', {
            'name': 'John Doe',
            'email': 'john@example.com',
            'phone': '1234567890'
        }, format='json')
        response = self.client.put('/api/investor/john@example.com/update/', {
            'name': 'John Doe Updated',
            'email': 'john@example.com',
            'phone': '0987654321'
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
