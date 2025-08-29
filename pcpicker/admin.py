from django.contrib import admin
from .models import CPU,GPU,CpuCooler,Motherboard,Ram,Storage,Case,PowerSupply,OperatingSystem,Monitor,CustomUser,SaveBuild

# Register the CPU model
admin.site.register(CPU)
admin.site.register(GPU)
admin.site.register(CpuCooler)
admin.site.register(Motherboard )
admin.site.register(Ram)
admin.site.register(Storage)
admin.site.register(Case )
admin.site.register (PowerSupply )
admin.site.register(OperatingSystem)
admin.site.register(Monitor)
admin.site.register(CustomUser)
admin.site.register(SaveBuild)

