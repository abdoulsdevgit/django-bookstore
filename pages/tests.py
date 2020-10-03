from django.http import response
from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve


# local imports
from .views import HomePageView, AboutPageView


class HomePageTest(SimpleTestCase):

    def setUp(self) -> None:
        url = reverse('home')
        self.response = self.client.get(reverse('home'))

    def test_homepage_status_code(self) -> None: 
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self) -> None:
        self.assertTemplateUsed(self.response, 'home.html')

    def test_homepage_contains_correct_html(self) -> None:
        self.assertContains(self.response, 'Homepage')


    def test_homepage_does_not_contain_incorrect_html(self):
        self.assertNotContains(
            self.response, 'Hi there! I should not be on the page.'
        )

    def test_homepage_url_resolves_homepageview(self):
        view = resolve('/')
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)

class AboutPageTest(TestCase):

    def setUp(self) -> None:
        url = reverse('about')
        self.response = self.client.get(url)

    def test_aboutpage_exist(self) -> None:
        self.assertAlmostEqual(self.response.status_code, 200)

    def test_homepage_template(self) -> None:
        self.assertTemplateUsed(self.response, 'about.html')

    def test_aboutpage_contains_correct_html(self) -> None: 
        self.assertContains(self.response, 'About Page')

    def test_aboutpage_does_not_contain_incorrect_html(self) -> None: 
        self.assertNotContains(self.response, 'Hi there! I should not be on the page.')

    def test_aboutpage_url_resolves_aboutpageview(self) -> None: 
        view = resolve('/about/')
        self.assertEqual(view.func.__name__,
            AboutPageView.as_view().__name__)
