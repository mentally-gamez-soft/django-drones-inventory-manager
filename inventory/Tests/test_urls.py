from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from inventory.views import home, DroneUpdateView, CameraUpdateView, CameraListView, DroneListView

class TestUrls(SimpleTestCase):

    def test_home_url_resolves(self):
        url = reverse('inventory-home')
        self.assertEqual(resolve(url).func, home)

    def test_drone_details_url_resolves(self):
        url = reverse('drone-update', args=['123'])
        self.assertEqual(resolve(url).func.view_class, DroneUpdateView)

    def test_camera_liste_url_resolves(self):
        url = reverse('camera-list')
        self.assertEqual(resolve(url).func.view_class, DroneListView)

    def test_camera_details_url_resolves(self):
        url = reverse('camera-update', args=['123'])
        self.assertEqual(resolve(url).func.view_class, CameraUpdateView)

    def test_camera_liste_url_resolves(self):
        url = reverse('camera-list')
        self.assertEqual(resolve(url).func.view_class, CameraListView)
