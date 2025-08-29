import pandas as pd
from django.core.management.base import BaseCommand
from pcpicker.models import CpuCooler, Motherboard, Ram, Storage, PowerSupply, Case, OperatingSystem, Monitor

class Command(BaseCommand):
    help = 'Import component data (excluding CPU and GPU) from CSV files into the database'

    def handle(self, *args, **kwargs):
        # Path to the CSV files
        cooler_df = pd.read_csv(r'C:\Users\pavit\programing\cpucoolers.csv', encoding='ISO-8859-1')  
        motherboard_df = pd.read_csv(r'C:\Users\pavit\programing\Motherboard.csv', encoding='ISO-8859-1')  
        memory_df = pd.read_csv(r'C:\Users\pavit\programing\Memory.csv', encoding='ISO-8859-1')  
        storage_df = pd.read_csv(r'C:\Users\pavit\programing\Storage.csv', encoding='ISO-8859-1')  
        case_df = pd.read_csv(r'C:\Users\pavit\programing\case.csv', encoding='ISO-8859-1')  
        psu_df = pd.read_csv(r'C:\Users\pavit\programing\Power supply.csv', encoding='ISO-8859-1')  
        os_df = pd.read_csv(r'C:\Users\pavit\programing\OS.csv', encoding='ISO-8859-1')  
        monitor_df = pd.read_csv(r'C:\Users\pavit\programing\Monitor.csv', encoding='ISO-8859-1')  

        # Step 1: Import CPU Cooler Data
        for _, row in cooler_df.iterrows():
            CpuCooler.objects.update_or_create(
                name=row['Name'],
                defaults={
                    'cooler_type': row['Type'],
                    'tdp': row['TDP Support (W)'],
                    'fan_size': row['Fan Size (mm)'],
                    'noise_level': row['Noise Level (dB)'],
                    'socket_compatibility': row['Socket Compatibility'],
                    'rpm_range': row['RPM Range'],
                    'fan_count': row['Number of Fans'],
                    'benchmark': row['Benchmark'],
                }
            )

        # Step 2: Import Motherboard Data
        for _, row in motherboard_df.iterrows():
            Motherboard.objects.update_or_create(
                name=row['Name'],
                defaults={
                    'socket_cpu': row['Socket/CPU'],
                    'form_factor': row['Form Factor'],
                    'memory_max': row['Memory Max'],
                    'memory_slots': row['Memory Slots'],
                    'color': row['Color'],
                    'benchmark': row['Benchmark'],
                }
            )

        # Step 3: Import Memory Data
        for _, row in memory_df.iterrows():
            Ram.objects.update_or_create(
                name=row['Name'],
                defaults={
                    'speed': row['Speed'],
                    'modules': row['Modules'],
                    'color': row['Color'],
                    'first_word_latency': row['First Word Latency'],
                    'cas_latency': row['CAS Latency'],
                    'benchmark': row['Benchmark'],
                }
            )

        # Step 4: Import Storage Data
        for _, row in storage_df.iterrows():
            Storage.objects.update_or_create(
                name=row['Name'],
                defaults={
                    'capacity': row['Capacity'],
                    'storage_type': row['Type'],
                    'cache': row['Cache'],
                    'form_factor': row['Form Factor'],
                    'interface': row['Interface'],
                    'benchmark': row['Benchmark'],
                }
            )

        # Step 5: Import PSU Data
        for _, row in psu_df.iterrows():
            PowerSupply.objects.update_or_create(
                name=row['Name'],
                defaults={
                    'efficiency_rating': row['Efficiency Rating'],
                    'wattage': row['Wattage'],
                    'modular': row['Modular'],
                    'color': row['Color'],
                    'benchmark': row['Benchmark'],
                }
            )

        # Step 6: Import Case Data
        for _, row in case_df.iterrows():
            Case.objects.update_or_create(
                name=row['Name'],
                defaults={
                    'case_type': row['Type'],
                    'color': row['Color'],
                    'power_supply': row['Power Supply'],
                    'side_panel': row['Side Panel'],
                    'external_volume': row['External Volume'],
                    'internal_bays': row['Internal 3.5" Bays'],
                    'benchmark': row['Benchmark'],
                }
            )

        # Step 7: Import Operating System Data
        for _, row in os_df.iterrows():
            OperatingSystem.objects.update_or_create(
                name=row['Name'],
                defaults={
                    'mode': row['Mode'],
                    'max_supported_memory': row['Maximum Supported Memory'],
                    'benchmark': row['Benchmark'],
                }
            )

        # Step 8: Import Monitor Data
        for _, row in monitor_df.iterrows():
            Monitor.objects.update_or_create(
                name=row['Name'],
                defaults={
                    'screen_size': row['Screen Size'],
                    'resolution': row['Resolution'],
                    'refresh_rate': row['Refresh Rate'],
                    
                    'panel_type': row['Panel Type'],
                    'aspect_ratio': row['Aspect Ratio'],
                    'benchmark': row['Benchmark'],
                }
            )

        self.stdout.write(self.style.SUCCESS('Successfully imported all component data (excluding CPU and GPU)'))
