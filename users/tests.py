from django.test import TestCase
from .views import user_client, user_supplier

# Clients Unittests.
class TestClients(TestCase):
    def test_user_client(self):
        name = "rogelio ortiz"
        expected = f"Client {name} number 1"
        self.assertEqual(user_client(name), expected)
        
    def test_user_supplier(self):
        name = "oliver ortiz"
        expected = f"Supplier {name} number 1"
        self.assertEqual(user_supplier(name), expected)