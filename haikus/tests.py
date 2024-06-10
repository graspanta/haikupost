from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import Haiku, Review

class HaikuTests(TestCase):
    
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'testuser',
            email = 'testuser@email.com',
            password = 'testpass123'
        )
        self.haiku = Haiku.objects.create(
            poem ='blah blah blah',
            author = self.user,
        )
        
        self.review = Review.objects.create(
            haiku = self.haiku,
            author = self.user,
            review = 'Superb!'
        )
        
    def test_haiku_listing(self):
        self.assertEqual(f'{self.haiku.poem}', 'blah blah blah')
        self.assertEqual(f'{self.haiku.author}', 'testuser')
        
    def test_haiku_list_view(self):
        response = self.client.get(reverse('haiku_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'blah blah blah')
        self.assertTemplateUsed(response, 'haikus/haiku_list.html')
        
    def test_haiku_detail_view(self):
        response = self.client.get(self.haiku.get_absolute_url())
        no_response = self.client.get('haikus/123456Seven')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'blah blah blah')
        self.assertContains(response, 'Superb!')
        self.assertTemplateUsed(response, 'haikus/haiku_detail.html')