from django.contrib import admin
from django.urls import path, include
from sorting.views import visualize_sorting

admin.site.site_header = "Sorting Visualizer Admin"
admin.site.site_title = "Admin Portal"
admin.site.index_title = "Welcome to Sorting Visualizer"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', visualize_sorting, name='visualize_sorting'),
]
