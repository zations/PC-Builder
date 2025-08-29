from django.db import models
from django.contrib.auth.models import User
import uuid
# CPU Model
class CPU(models.Model):
    name = models.CharField(max_length=100)
    cpu_mark = models.IntegerField(default=0)
    tdp = models.FloatField(default=0.0)
    socket = models.CharField(max_length=100)
    cores = models.IntegerField(default=0)

    def __str__(self):
        return self.name

# GPU Model
class GPU(models.Model):
    name = models.CharField(max_length=100)
    G3mark = models.IntegerField(default=0)
    G2mark = models.IntegerField(default=0)
    Tdp = models.FloatField(null=True, blank=True, default=170)  # Fixed default value

    def __str__(self):
        return self.name

# CPU Cooler Model
class CpuCooler(models.Model):
    name = models.CharField(max_length=100)
    cooler_type = models.CharField(max_length=50)
    tdp = models.CharField(max_length=10)
    fan_size = models.CharField(max_length=10)
    noise_level = models.CharField(max_length=10)
    socket_compatibility = models.CharField(max_length=100)
    rpm_range = models.CharField(max_length=50)
    fan_count = models.IntegerField(default=1)
    benchmark = models.IntegerField(null=True, blank=True, default=94)  # Fixed default value

    def __str__(self):
        return self.name

# Motherboard Model
class Motherboard(models.Model):
    name = models.CharField(max_length=100)
    socket_cpu = models.CharField(max_length=50)
    form_factor = models.CharField(max_length=50)
    memory_max = models.CharField(max_length=10)
    memory_slots = models.IntegerField(default=0)
    color = models.CharField(max_length=50)
    benchmark = models.IntegerField(default=0)

    def __str__(self):
        return self.name

# RAM Model
class Ram(models.Model):
    name = models.CharField(max_length=100)
    speed = models.CharField(max_length=10)
    modules = models.CharField(max_length=20)
    price_per_gb = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    color = models.CharField(max_length=20)
    first_word_latency = models.CharField(max_length=10)
    cas_latency = models.CharField(max_length=10)
    benchmark = models.IntegerField(default=0)

    def __str__(self):
        return self.name

# Storage Model
class Storage(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.CharField(max_length=10)
    storage_type = models.CharField(max_length=20)
    cache = models.CharField(max_length=20)
    form_factor = models.CharField(max_length=20)
    interface = models.CharField(max_length=50)
    benchmark = models.IntegerField(default=0)

    def __str__(self):
        return self.name

# Case Model
class Case(models.Model):
    name = models.CharField(max_length=100)
    case_type = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    power_supply = models.CharField(max_length=50)
    side_panel = models.CharField(max_length=50)
    external_volume = models.CharField(max_length=50)
    internal_bays = models.IntegerField(default=0)
    benchmark = models.IntegerField(default=0)

    def __str__(self):
        return self.name

# Power Supply Model
class PowerSupply(models.Model):
    name = models.CharField(max_length=100)
    psu_type = models.CharField(max_length=50)
    efficiency_rating = models.CharField(max_length=20)
    wattage = models.CharField(max_length=100)
    modular = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    benchmark = models.IntegerField(default=0)

    def __str__(self):
        return self.name

# Operating System Model
class OperatingSystem(models.Model):
    name = models.CharField(max_length=100)
    mode = models.CharField(max_length=50)
    max_supported_memory = models.CharField(max_length=50)
    benchmark = models.IntegerField(default=0)

    def __str__(self):
        return self.name

# Monitor Model
class Monitor(models.Model):
    name = models.CharField(max_length=100)
    screen_size = models.CharField(max_length=10)
    resolution = models.CharField(max_length=50)
    refresh_rate = models.CharField(max_length=10)
    response_time = models.CharField(max_length=10)
    panel_type = models.CharField(max_length=50)
    aspect_ratio = models.CharField(max_length=10)
    benchmark = models.IntegerField(default=0)

    def __str__(self):
        return self.name

# PC Build Model



class CustomUser(models.Model):
    user_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  

    def __str__(self):
        return self.name    

class PCBuild(models.Model):

    session_id = models.CharField(max_length=255, unique=True)
    selected_cpu = models.CharField(max_length=255, null=True, blank=True)
    selected_gpu = models.CharField(max_length=255, null=True, blank=True)
    selected_motherboard = models.CharField(max_length=255, null=True, blank=True)
    selected_ram = models.CharField(max_length=255, null=True, blank=True)
    selected_storage = models.CharField(max_length=255, null=True, blank=True)
    selected_case = models.CharField(max_length=255, null=True, blank=True)
    selected_psu = models.CharField(max_length=255, null=True, blank=True)
    selected_os = models.CharField(max_length=255, null=True, blank=True)
    selected_cpu_cooler = models.CharField(max_length=255, null=True, blank=True)
    selected_monitor = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"PC Build (Session {self.session_id})"
class SaveBuild(models.Model):
    user_id = models.CharField(max_length=100 , default=121) 
    build_name = models.CharField(max_length=100, default="My Build")
    selected_cpu = models.CharField(max_length=255, null=True, blank=True)
    selected_gpu = models.CharField(max_length=255, null=True, blank=True)
    selected_motherboard = models.CharField(max_length=255, null=True, blank=True)
    selected_ram = models.CharField(max_length=255, null=True, blank=True)
    selected_storage = models.CharField(max_length=255, null=True, blank=True)
    selected_case = models.CharField(max_length=255, null=True, blank=True)
    selected_psu = models.CharField(max_length=255, null=True, blank=True)
    selected_os = models.CharField(max_length=255, null=True, blank=True)
    selected_cpu_cooler = models.CharField(max_length=255, null=True, blank=True)
    selected_monitor = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.build_name}"

class Live_CPU(models.Model):
    name = models.CharField(max_length=100)
    cpu_mark=models.CharField(max_length=100)
    tdp = models.IntegerField(default=0)
    socket = models.CharField(max_length=100)
    cores = models.IntegerField(default=0)

    def __str__(self):
        return self.name