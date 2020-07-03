''' Tutorial ==>  https://www.youtube.com/watch?v=IKnp2ckuhzg&list=PLbpAWbHbi5rMF2j5n6imm0enrSD9eQUaM&index=4'''

from django.test import TestCase
from inventory.models import CameraProduct, DroneProduct

class TestModels(TestCase):

    def setUp(self):
        self.camera15 = CameraProduct.objects.create(
            brand='Sony',
            model='A700 DSLR',
            camera_resolution='12 Mpx',
        )

        self.camera16 = CameraProduct.objects.create(
            brand='Sony',
            model='A900 DSLR',
            camera_resolution='24 Mpx',
        )

        self.drone17 = DroneProduct.objects.create(
            brand='DJI',
            model='Mavic Ari 2',
            serial_number='00034562WERT',
        )

    def test_cameraproduct_is_assigned_date_on_creation(self):
        self.assertIsNotNone(self.camera15.added_date)

    def test_droneproduct_is_assigned_date_on_creation(self):
        self.assertIsNotNone(self.drone17.added_date)

    def test_drone_is_linked_to_camera(self):
        self.drone17.compatible_camera.set([self.camera15.pk, self.camera16.pk])
        self.assertEqual(self.drone17.compatible_camera.count(), 2)
