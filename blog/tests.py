from django.test import TestCase
from django.contrib.auth.models import User
from . models import Post, Category

# Create your tests here.
class Test_CreatePost(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_category = Category.objects.create(name = "django")
        test_user = User.objects.create_user(username = "testuser", password = "test123")
