from django.test import SimpleTestCase

# Create your tests here.
class PageTest(SimpleTestCase):
    def test_urls(self):
        response = self.client.get("/message/")
        self.assertEqual(response.status_code, 200)