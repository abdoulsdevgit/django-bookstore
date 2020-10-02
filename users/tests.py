from django.test import TestCase
from django.contrib.auth import get_user_model

class CustomUserTests(TestCase):
    
    def test_create_user(self):

        User = get_user_model()
        user = User.objects.create(
            username="will",
            email="will@example.com",
            password="abc123"
        )

        self.assertEqual(user.username, 'will')
        self.assertEqual(user.email, 'will@example.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)


    def test_create_superuser(self):

        User = get_user_model()
        user = User.objects.create_superuser(
            username="superadmin",
            email="superuser@example.com",
            password="abc123"
        )

        self.assertEqual(user.username, 'superadmin')
        self.assertEqual(user.email, 'superuser@example.com')
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
