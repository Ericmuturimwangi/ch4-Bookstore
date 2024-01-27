from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
# Create your tests here.

class UserTests (TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username = 'EM', email='em@em.com', password= '1234'
        )
        self.assertEqual(user.username, "EM")
        self.assertEqual(user.email, "em@em.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
        username="EM", email="em@em.com",
        password="1234"
        )
        self.assertEqual(admin_user.username, "EM")
        self.assertEqual(admin_user.email, "em@em.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)



