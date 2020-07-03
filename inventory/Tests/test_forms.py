from django.test import SimpleTestCase
from inventory.forms import DroneCreationForm, CameraCreationForm, SearchCamerasForm, SearchDroneForm


class TestForms(SimpleTestCase):

    def test_drone_creation_form_valid_Data(self):
        form = DroneCreationForm(data={
            'brand': 'AUTEL',
            'model': 'Robotics EVO',
            'serial_number': 'Y2ERBVT5678',
        })

        self.assertTrue(form.is_valid())

    def test_drone_creation_form_invalid_Data(self):
        form = DroneCreationForm(data={
            'brand': '',
            'model': '',
            'serial_number': 'Y2ERBVT5678',
        })

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)

    def test_drone_creation_form_no_data(self):
        form = DroneCreationForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)

    def test_camera_creation_form_valid_Data(self):
        form = CameraCreationForm(data={
            'brand': 'Panasonic',
            'model': 'S1',
            'camera_resolution': '24 Mpx',
        })

        self.assertTrue(form.is_valid())

    def test_camera_creation_form_invalid_Data(self):
        form = CameraCreationForm(data={
            'brand': 'Panasonic',
            'model': 'S1',
            'camera_resolution': '',
        })

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)

    def test_camera_creation_form_no_data(self):
        form = CameraCreationForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)

    def test_search_camera_form_valid_Data(self):
        form = SearchCamerasForm(data={
            'brand': 'Panasonic',
            'model': 'S1',
            'camera_resolution': '24 Mpx',
        })

        self.assertTrue(form.is_valid())

    def test_search_camera_form_no_data(self):
        form = SearchCamerasForm(data={})

        self.assertTrue(form.is_valid())

    def test_search_drone_form_valid_Data(self):
        form = SearchDroneForm(data={
            'brand': 'Panasonic',
            'model': 'S1',
            'serial_number': '123456',
        })

        self.assertTrue(form.is_valid())

    def test_search_drone_form_no_data(self):
        form = SearchDroneForm(data={})

        self.assertTrue(form.is_valid())
