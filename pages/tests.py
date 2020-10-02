from django.http import response
from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve


# local imports
from .views import HomePageView


class HomePageTest(SimpleTestCase):

    def setUp(self) -> None:
        url = reverse('home')
        self.response = self.client.get(reverse('home'))

    def test_homepage_status_code(self) -> None: 
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, 'home.html')

    def test_homepage_contains_correct_html(self):
        self.assertContains(self.response, 'Homepage')


    def test_homepage_does_not_contain_incorrect_html(self):
        self.assertNotContains(
            self.response, 'Hi there! I should not be on the page.'
        )

    def test_homepage_url_resolves_homepageview(self):
        view = resolve('/')
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)
