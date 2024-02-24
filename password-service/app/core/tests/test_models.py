from django.test import TestCase
from core.models import LoginCredential
import uuid


class LoginCredentialModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        LoginCredential.objects.create(user_id=uuid.uuid4(),
                                       link='test_link', email='test_email',
                                       password='test_password')

    def test_link_label(self):
        login_credential = LoginCredential.objects.get(id=1)
        field_label = login_credential._meta.get_field('link').verbose_name
        self.assertEquals(field_label, 'link')

    def test_email_label(self):
        login_credential = LoginCredential.objects.get(id=1)
        field_label = login_credential._meta.get_field('email').verbose_name
        self.assertEquals(field_label, 'email')

    def test_password_label(self):
        login_credential = LoginCredential.objects.get(id=1)
        field_label = login_credential._meta.get_field('password').verbose_name
        self.assertEquals(field_label, 'password')
