from django.contrib import admin
from .models import CameraProduct, Product, DroneProduct


admin.site.register(Product)
admin.site.register(CameraProduct)
admin.site.register(DroneProduct)
