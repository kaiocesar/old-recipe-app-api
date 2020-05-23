from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):

    def test_create_user_with_email_successful(self):
        email = 'kaio@cesar.com.br'
        password = 'T123Kaio456'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        email = 'kaio@CESAR.COM.BR'
        user = get_user_model().objects.create_user(email, 'Test123')

        self.assertEqual(user.email, email.lower())
