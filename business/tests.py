from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from django.core.exceptions import ValidationError
from .models import Value

class ValueAPITestCase(APITestCase):
    def setUp(self):
        self.value = Value.objects.create(timestamp='2024-02-19T10:00:00', value=42.0)

    def test_get_values(self):
        response = self.client.get('/api/values/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_value(self):
        data = {'timestamp': '2024-02-19T11:00:00', 'value': 50.0}
        response = self.client.post('/api/values/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Value.objects.count(), 2)

class ValueModelTestCase(TestCase):
    def test_invalid_timestamp(self):
        with self.assertRaises(ValidationError):
            Value.objects.create(timestamp='invalid_date_format', value=42.0)
    
    def test_invalid_value(self):
        with self.assertRaises(ValueError):
            Value.objects.create(timestamp='2024-02-19T10:00:00', value='incorrect value')

    def setUp(self):
        self.value = Value.objects.create(timestamp='2024-02-19T10:00:00', value=42.0)

    def test_value_creation(self):
        self.assertEqual(Value.objects.count(), 1)
        self.assertEqual(self.value.timestamp, '2024-02-19T10:00:00')
        self.assertEqual(self.value.value, 42.0)