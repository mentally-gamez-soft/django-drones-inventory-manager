from django import forms

from .models import CameraProduct, DroneProduct


class DroneCreationForm(forms.ModelForm):
    '''Formulaire pour creer des drones'''
    class Meta:
        model = DroneProduct
        fields = ['brand', 'model', 'serial_number']


class CameraCreationForm(forms.ModelForm):
    '''Formulaire pour creer des cameras'''
    class Meta:
        model = CameraProduct
        fields = ['brand', 'model', 'camera_resolution']


''' Formulaire pour rechercher des cameras '''
class SearchCamerasForm(forms.Form):

    brand = forms.CharField(required=False)
    model = forms.CharField(required=False)
    resolution = forms.CharField(required=False)


class SearchDroneForm(forms.Form):

    brand = forms.CharField(required=False)
    model = forms.CharField(required=False)
    serial_number = forms.CharField(required=False)
