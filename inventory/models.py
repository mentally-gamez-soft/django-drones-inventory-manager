from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.urls import reverse


class Product(models.Model):
    brand = models.CharField(max_length=100, blank=False, null=False, default="Sony")
    model = models.CharField(max_length=100, blank=False, null=False, default="Axxx")
    added_date = models.DateTimeField(null=False, blank=True, default=timezone.now)
    added_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    last_updated = models.DateTimeField(null=True, blank=True)
    last_updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='lastUser')

    class Meta:
        ordering = ['brand', 'model']
        indexes = [
            models.Index(fields=['added_date'], name='added_date_idx'),
            models.Index(fields=['brand'], name='brand_idx'),
            models.Index(fields=['model'], name='model_idx'),
            models.Index(fields=['brand', 'model'], name='brand_model_idx'),
        ]

    def get_absolute_url(self):
        '''Permet de d indiquer a Django que la vue doit gerer le rerouting apres click sur creation d un nouveau produit '''
        return reverse('inventory-home')


class CameraProduct(Product):
    camera_resolution = models.CharField(max_length=8, blank=False, null=False, default="12 mpx")

    objects = models.Manager()  # The default manager.

    def __str__(self):
        return 'Camera - Brand: {} - Model: {} - Resolution: {}'.format(self.brand, self.model, self.camera_resolution)


class DroneProduct(Product):
    serial_number = models.CharField(max_length=100, blank=False, null=False, default="0000000000")
    compatible_camera = models.ManyToManyField(CameraProduct)

    objects = models.Manager()  # The default manager.

    def __str__(self):
        return 'Drone - Brand: {} - Model: {} - serial number: {}'.format(self.brand, self.model, self.serial_number)
