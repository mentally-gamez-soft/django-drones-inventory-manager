from django.test import TestCase, Client
from django.urls import reverse
from inventory.models import CameraProduct, DroneProduct


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.camera_list_url = reverse('camera-list')
        self.camera_update_url = reverse('camera-update', args=['15'])
        self.camera15 = CameraProduct.objects.create(
            brand='Sony',
            model='A700 DSLR',
            camera_resolution='12 Mpx'
        )

        self.drone_list_url = reverse('drone-list')
        self.drone_update_url = reverse('drone-update', args=['16'])
        self.drone16 = DroneProduct.objects.create(
            brand='DJI',
            model='Inspire 2',
            serial_number='986123000NMH'
        )

    def test_camera_list_get(self):
        response = self.client.get(self.camera_list_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'inventory/cameraproduct_list.html')

    def test_drone_list_get(self):
        response = self.client.get(self.drone_list_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'inventory/droneproduct_list.html')

    def test_camera_update(self):
        response = self.client.get(self.camera_update_url)

        self.assertEqual(response.status_code, 302)  # redirect after update

    def test_drone_update(self):
        response = self.client.get(self.drone_update_url)

        self.assertEqual(response.status_code, 302)  # redirect after update
