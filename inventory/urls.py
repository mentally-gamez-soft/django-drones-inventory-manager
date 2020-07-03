from django.urls import path
from inventory.views import home, CameraAddView, CameraUpdateView, CameraListView, DroneAddView, DroneListView, DroneUpdateView

urlpatterns = [
    path('', home, name="inventory-home"),
    path('camera/create/', CameraAddView.as_view(), name='camera-add'),
    path('camera/<int:pk>/update/', CameraUpdateView.as_view(), name='camera-update'),
    path('cameras/', CameraListView.as_view(), name='camera-list'),
    path('drone/create/', DroneAddView.as_view(), name='drone-add'),
    path('drones/', DroneListView.as_view(), name='drone-list'),
    path('drone/<int:pk>/update/', DroneUpdateView.as_view(), name='drone-update'),
]
