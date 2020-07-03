from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import CameraProduct, DroneProduct
from .forms import CameraCreationForm, SearchCamerasForm, DroneCreationForm, SearchDroneForm
from datetime import datetime
from django.urls import reverse


def home(request):
    ''' The homepage will display a set of informational summaries and links to update the data '''
    l_cameras = CameraProduct.objects.all()
    nb_cameras = l_cameras.count()
    l_cameras = l_cameras[:5]

    l_drones = DroneProduct.objects.all()
    nb_drones = l_drones.count()
    l_drones_temp = l_drones[:5]

    return render(request, 'inventory/index.html', {'nb_cameras': nb_cameras,
                                                    'l_cameras': l_cameras,
                                                    'nb_drones': nb_drones,
                                                    'l_drones': l_drones,
                                                    }
                  )


class DroneAddView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = DroneProduct
    form_class = DroneCreationForm

    def form_valid(self, form):
        input_keys = [key for key in self.request.POST if key.startswith("camera-")]

        form.instance.added_by = self.request.user

        if super().form_valid(form):
            form.instance.save()

            if len(input_keys) > 0:
                for key in input_keys:
                    id_key = key[key.find('-') + 1:len(key)]
                    print(id_key)
                    form.instance.compatible_camera.add(CameraProduct.objects.get(id=id_key))

        return super().form_valid(form)

    # Verifie que user est dans le groupe des support_team
    def test_func(self):
        return self.request.user.groups.filter(name='support_team').exists()

    def get_context_data(self, **kwargs):
        context = super(DroneAddView, self).get_context_data(**kwargs)
        l_cameras = CameraProduct.objects.all().values('id', 'brand', 'model', 'camera_resolution')
        context.update({
            'l_cameras': l_cameras,
        })
        return context


class DroneUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = DroneProduct
    form_class = DroneCreationForm

    def form_valid(self, form):
        input_keys = [key for key in self.request.POST if key.startswith("camera-")]
        form.instance.last_updated_by = self.request.user
        form.instance.last_updated = datetime.now()

        print(self.request.POST)

        if super().form_valid(form):
            all_cameras = self.get_object().compatible_camera.all()
            for camera in all_cameras:
                form.instance.compatible_camera.remove(camera)

            form.instance.save()

            if len(input_keys) > 0:
                for key in input_keys:
                    id_key = key[key.find('-') + 1:len(key)]
                    form.instance.compatible_camera.add(CameraProduct.objects.get(id=id_key))

        return super().form_valid(form)

    # Verifie que user est dans le groupe des support_team
    def test_func(self):
        return self.request.user.groups.filter(name='support_team').exists()

    def get_context_data(self, **kwargs):
        current_cameras = self.get_object().compatible_camera.all().values('id')

        context = super(DroneUpdateView, self).get_context_data(**kwargs)
        l_cameras = CameraProduct.objects.all().values('id', 'brand', 'model', 'camera_resolution')

        resulting_cameras = list()

        for camera in l_cameras:
            if current_cameras.filter(id=camera['id']).exists():
                resulting_cameras.append({'id': camera['id'], 'brand': camera['brand'], 'model': camera['model'], 'camera_resolution': camera['camera_resolution'], 'provisionned': True})
            else:
                resulting_cameras.append({'id': camera['id'], 'brand': camera['brand'], 'model': camera['model'], 'camera_resolution': camera['camera_resolution'], 'provisionned': False})

        context.update({
            'l_cameras': resulting_cameras,
        })
        return context


class DroneListView(ListView):
    model = DroneProduct
    paginate_by = 10

    def get(self, *args, **kwargs):
        filter_brand = self.request.GET.get('brand')
        filter_model = self.request.GET.get('model')
        filter_serial_number = self.request.GET.get('serial_number')
        sort_results = self.request.GET.get('sort')

        object_list = DroneProduct.objects.all()

        if filter_brand:
            object_list = object_list.filter(brand__icontains=filter_brand)

        if filter_model:
            object_list = object_list.filter(model__icontains=filter_model)

        if filter_serial_number:
            object_list = object_list.filter(serial_number__icontains=filter_serial_number)

        form_search_drone = SearchDroneForm(self.request.GET)

        if sort_results:
            context = {
                'form': form_search_drone,
                'object_list': object_list,
                'sorted': sort_results,
            }
        else:
            context = {
                'form': form_search_drone,
                'object_list': object_list,
            }

        return render(self.request, "inventory/droneproduct_list.html", context)


class CameraAddView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = CameraProduct
    form_class = CameraCreationForm

    def form_valid(self, form):
        form.instance.added_by = self.request.user
        return super().form_valid(form)

    # Verifie que user est dans le groupe des support_team
    def test_func(self):
        return self.request.user.groups.filter(name='support_team').exists()


class CameraUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = CameraProduct
    form_class = CameraCreationForm

    def form_valid(self, form):
        form.instance.last_updated_by = self.request.user
        form.instance.last_updated = datetime.now()
        return super().form_valid(form)

    # Verifie que user est dans le groupe des support_team
    def test_func(self):
        return self.request.user.groups.filter(name='support_team').exists()

# page listing the products


class CameraListView(ListView):
    model = CameraProduct
    paginate_by = 10

    def get(self, *args, **kwargs):
        filter_brand = self.request.GET.get('brand')
        filter_model = self.request.GET.get('model')
        filter_resolution = self.request.GET.get('resolution')
        sort_results = self.request.GET.get('sort')

        object_list = CameraProduct.objects.all()

        if filter_brand:
            object_list = object_list.filter(brand__icontains=filter_brand)

        if filter_model:
            object_list = object_list.filter(model__icontains=filter_model)

        if filter_resolution:
            object_list = object_list.filter(camera_resolution__icontains=filter_resolution)

        form_search_camera = SearchCamerasForm(self.request.GET)

        if sort_results:
            context = {
                'form': form_search_camera,
                'object_list': object_list,
                'sorted': sort_results,
            }
        else:
            context = {
                'form': form_search_camera,
                'object_list': object_list,
            }

        return render(self.request, "inventory/cameraproduct_list.html", context)
