from django.contrib import admin
from .models import About, Lessor, Lessee, Truck, Onhire, Booktruck, Driver


admin.site.register(About)
admin.site.register(Lessor)
admin.site.register(Lessee)
admin.site.register(Truck)
admin.site.register(Driver)
admin.site.register(Onhire)
admin.site.register(Booktruck)