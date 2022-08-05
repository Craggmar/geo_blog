from django.test import TestCase
from django.contrib.auth.models import User
from users.models import BlogUser

class TestUser(TestCase):
  def test_create(self):
    user = User.objects.create(username='testuser', password='T3stUs3rpass', email="testuser")
    self.assertEqual(User.objects.get(username='testuser'), user)

  
