from rest_framework import serializers
from rest_framework.test import APIClient, APISimpleTestCase, APITestCase
from .serializers import BondSerializer
from django.contrib.auth.models import User
from django.test import RequestFactory
from datetime import datetime
from rest_framework.reverse import reverse
from rest_framework import status


class HomePage(APISimpleTestCase):
    def test_root(self):
        resp = self.client.get("")
        assert resp.status_code == 200

class BondTest(APITestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(username="test", password="test")
        self.bond = {
            "userid": self.test_user.id, 
            "isin": "FR0000131104",
            "size": 100000000,
            "currency": "EUR",
            "maturity": "2025-02-28",
            "lei": "R0MUWSFPU8MPRO8K5P83", 
            "legal_name": "BNP PARIBAS"
        }
        self.factory = RequestFactory()
        self.request = self.factory.get('')
        self.request.user = self.test_user


    def test_valid_bond(self):
        serializer = BondSerializer(data=self.bond, context={"request": self.request})
        valid = serializer.is_valid()
        self.assertEqual(serializer.errors, {})
    
    def test_valid_lei(self):
        self.bond['lei'] = "R0MUWSFPU8MPR!!!###@"
        serializer = BondSerializer(data=self.bond, context={"request": self.request})
        valid = serializer.is_valid()
        self.assertNotEqual(serializer.errors, {})
    
    def test_valid_currency(self):
        self.bond['currency'] = "ABC"
        serializer = BondSerializer(data=self.bond, context={"request": self.request})
        valid = serializer.is_valid()
        self.assertNotEqual(serializer.errors, {})

    def test_valid_isin(self):
        self.bond['isin'] = "FR124xe4000131104"
        serializer = BondSerializer(data=self.bond, context={"request": self.request})
        valid = serializer.is_valid()
        self.assertNotEqual(serializer.errors, {})

    def test_valid_maturity(self):
        self.bond['maturity'] = datetime.today()
        serializer = BondSerializer(data=self.bond, context={"request": self.request})
        valid = serializer.is_valid()
        self.assertNotEqual(serializer.errors, {})

class AuthenticationTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="test", password="test")
        self.client = APIClient()
    
    def set_authenticated(self):
        self.client.force_authenticate(user=self.user)

    def set_not_authenticated(self):
        self.client.force_authenticate(user=None)

    def test_authenitcated(self):
        self.set_authenticated()
        response = self.client.get(reverse('bonds'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_not_authenitcated(self):
        self.set_not_authenticated()
        response = self.client.get(reverse('bonds'))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

class BondAPI(APITestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(username="test", password="test")
        self.bond_post = {
            "isin": "FR0000131104",
            "size": 100000000,
            "currency": "EUR",
            "maturity": "2025-02-28",
            "lei": "R0MUWSFPU8MPRO8K5P83"
        }
        self.bond_get = {
            "isin": "FR0000131104",
            "size": 100000000,
            "currency": "EUR",
            "maturity": "2025-02-28",
            "lei": "R0MUWSFPU8MPRO8K5P83",
            "legal_name": 'BNP PARIBAS'
        }
        self.client = APIClient()
        self.client.force_authenticate(self.test_user)


    def test_post_get_bond(self):
        res = self.client.post(reverse('bonds'), self.bond_post, format='json')
        self.assertEqual(res.status_code, status.HTTP_200_OK)

        res = self.client.get(reverse('bonds'))
        self.assertEqual([dict(bond) for bond in res.data], [self.bond_get])

    def test_post_lei_not_found(self):
        self.bond_post["lei"] = "XXXXXXXXXXXXXXXXX"
        res = self.client.post(reverse('bonds'), self.bond_post, format='json')
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)