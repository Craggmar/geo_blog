from django.test import TestCase

# Create your tests here.

class URLStaticTests(TestCase):
  def test_checkindex(self):
    response = self.client.get('/0/')
    self.assertEqual(response.status_code, 200)

  def test_checkabout(self):
    response = self.client.get('/about/')
    self.assertEqual(response.status_code, 200)

  def test_checkgallery(self):
    response = self.client.get('/gallery/')
    self.assertEqual(response.status_code, 200)

  def test_checkterms(self):
    response = self.client.get('/terms/')
    self.assertEqual(response.status_code, 200)
  
  def test_checknewtopic(self):
    response = self.client.get('/new_topic/')
    self.assertEqual(response.status_code, 200)

class URLDynamicTests(TestCase):

  def test_checktopic(self):
    response = self.client.get('/topic/(15)/')
    self.assertEqual(response.status_code, 200)
  
  def test_checkedittopic(self):
    response = self.client.get('/edit_topic/15/')
    self.assertEqual(response.status_code, 200)
  
  def test_checkdeletetopic(self):
    response = self.client.get('/delete_topic/(15)/')
    self.assertEqual(response.status_code, 200)