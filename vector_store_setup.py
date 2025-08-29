import os
import django
from langchain.schema import Document


# Step 1: Django setup
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pcpickertool.settings")
django.setup()

# Step 2: Load website content
with open("websiteinfo.txt", "r", encoding="utf-8") as f:
    website_info = f.read()

# Step 3: Import your models
from pcpicker.models import CPU, GPU, Ram, Motherboard, Case, PowerSupply, OperatingSystem, Monitor, Storage, CpuCooler , SaveBuild
# CPU, GPU, Ram, Motherboard, Case, PowerSupply, OperatingSystem, Monitor, Storage, CpuCooler,SaveBuild
# Step 4: Gather data
cpu_data  = []

for row in CPU.objects.all() :
          context = (
            f"The CPU '{row.name}' has a CPU Mark score of {row.cpu_mark}, "
            f"{row.cores} cores, and uses the '{row.socket}' socket. "
            f"It has a thermal design power (TDP) of {row.tdp} watts."
        )
          
          cpu_data.append(Document(page_content=context,metadata={"component": "CPU"}))

# GPU_data=[]
# for row in GPU.objects.all():
#       # model should be the list of GPU rows as dicts
#         context = f"The GPU '{row.name}' has a G3Mark score of {row.G3mark}, "
#         f"a G2Mark score of {row.G2mark}, and a TDP of {row.Tdp}W."
#         GPU_data.append(Document(page_content=context,metadata={"component": "GPU"}))

# CPUCOOLER_data = []
# for row in CpuCooler.objects.all():  # model should be a list of CPU cooler rows as dictionaries
#     context = (
#             f"The CPU cooler '{row.name}' has a fan size of {row.fan_size}, "
#             f"noise level of {row.noise_level} dB, supports sockets {row.socket_compatibility}, "
#             f"and operates in the RPM range {row.rpm_range}. It is a {row.cooler_type} cooler "
#             f"with a TDP rating of {row.tdp}W, benchmark score {row.benchmark}, and has {row.fan_count} fans."
#     )
#     CPUCOOLER_data.append(Document(page_content=context,metadata={"component": "CPUCOOLER"}))
    
# CASE_data = []
# for row in Case.objects.all():  # model should be a list of case rows as dictionaries
#     context = (
#             f"The PC case '{row.name}' is a {row.case_type} type with color {row.color}. "
#             f"It includes a power supply: {row.power_supply}, side panel type: {row.side_panel}, "
#             f"external volume of {row.external_volume}, benchmark score of {row.benchmark}, "
#             f"and {row.internal_bays} internal bays."
#     )
#     CASE_data.append(Document(page_content=context,metadata={"component": "CASE"}))

# MONITOR_data = []
# for row in Monitor.objects.all():  # model should be a list of monitor rows as dictionaries
#     context = (
#             f"The monitor '{row.name}' has a screen size of {row.screen_size}, "
#             f"resolution {row.resolution}, refresh rate {row.refresh_rate}, "
#             f"response time {row.response_time}, panel type {row.panel_type}, "
#             f"aspect ratio {row.aspect_ratio}, and a benchmark score of {row.benchmark}."
#     )
#     MONITOR_data.append(Document(page_content=context,metadata={"component": "MONITOR"}))

# MOTHERBOARD_data = []
# for row in Motherboard.objects.all():  # model should be a list of motherboard rows as dictionaries
#     context = (
#             f"The motherboard '{row.name}' supports socket type {row.socket_cpu}, "
#             f"has a {row.form_factor} form factor, supports up to {row.memory_max} of memory, "
#             f"is available in {row.color} color, includes {row.memory_slots} memory slots, "
#             f"and has a benchmark score of {row.benchmark}.")
#     MOTHERBOARD_data.append(Document(page_content=context,metadata={"component": "MOTHERBOARD"}))

# OS_data = []
# for row in OperatingSystem.objects.all():  # model should be a list of operating system rows as dictionaries
#     context = (
#          f"The operating system '{row.name}' runs in {row.mode} mode, supports up to "
#          f"{row.max_supported_memory} of memory, and has a benchmark score of {row.benchmark}.")
#     OS_data.append(Document(page_content=context,metadata={"component": "OS"}))

# PSU_data = []
# for row in PowerSupply.objects.all():  # model is your list of power supply dict rows
#     context = (
#             f"The power supply '{row.name}' is a {row.psu_type} unit with {row.wattage} wattage, "
#             f"{row.efficiency_rating} efficiency rating, modular: {row.modular}, "
#             f"color: {row.color}, and a benchmark score of {row.benchmark}."
#     )
#     PSU_data.append(Document(page_content=context,metadata={"component": "PSU"}))

# RAM_data = []
# for row in Ram.objects.all():  # model should be your list of RAM dict rows
#     context = (
#             f"The RAM module '{row.name}' runs at {row.speed} with configuration {row.modules}. "
#             f"It has a price per GB of {row.price_per_gb}, comes in {row.color} color, "
#             f"a first word latency of {row.first_word_latency}, and CAS latency of {row.cas_latency}."
#             f"and a benchmark score of {row.benchmark}."
#     )
#     RAM_data.append(Document(page_content=context,metadata={"component": "RAM"}))

# STORAGE_data = []
# for row in Storage.objects.all():  # model should be a list of storage dicts
#     context = (
#             f"The storage device '{row.name}' has a capacity of {row.capacity}, "
#             f"uses {row.storage_type} type, features a cache of {row.cache}, "
#             f"has a form factor of {row.form_factor}, and connects via {row.interface}. "
#             f"It has a benchmark score of {row.benchmark}."
#     )
#     STORAGE_data.append(Document(page_content=context,metadata={"component": "STORAGE"}))




# Step 5: Combine all data
Webiste_data = website_info 
all_components = []

for component_list in [
    cpu_data,
    # GPU_data,
    # RAM_data,
    # PSU_data,
    # MONITOR_data,
    # CASE_data,
    # CPUCOOLER_data,
    # MOTHERBOARD_data,
    # STORAGE_data,
    # OS_data
]:
    all_components.extend(component_list)

# Step 6: Convert to chunks
from langchain.text_splitter import RecursiveCharacterTextSplitter
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
documents = text_splitter.create_documents(Webiste_data)

# Step 7: Create embeddings and vector store
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
Component_vector_db = FAISS.from_documents(
    documents=all_components,  # No need to wrap each item again
    embedding=embeddings
)
website_vector_db = FAISS.from_documents(
    documents=[Document(page_content=item, metadata={"source": "website"}) for item in Webiste_data],
    embedding=embeddings
)

# Step 8: Save vector store
Component_vector_db.save_local("pc_componet_vector_store")
website_vector_db.save_local("pc_website_vector_store")