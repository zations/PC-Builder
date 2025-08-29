from django.shortcuts import render
from .models import Case,CPU,GPU,CpuCooler,Motherboard,Monitor,Ram,OperatingSystem,PowerSupply,Storage,SaveBuild, CustomUser,Live_CPU
from django.shortcuts import redirect, render
from .groq_integration import check_compatibility_with_groq
from django.http import JsonResponse
from .models import Live_CPU


from .forms import RegisterForm

from .forms import LoginForm
from .models import CustomUser
import random

def index_view(request):
    """Render the home page."""
    return render(request, 'pc/index.html')



def cpu_list_view(request):
    cpus = CPU.objects.all()
    lcpus=Live_CPU.objects.all()
   
    return render(request, 'pc/cpu.html', {'cpus': cpus ,'lcpus':lcpus})

def cpucooler_list_view(request):
    cpu_coolers = CpuCooler.objects.all()  # Fetch all CPU data from your SQLite database
    return render(request, 'pc/cpucooler.html', {'Cpu_coolers': cpu_coolers})

def gpu_list_view(request):
    gpus = GPU.objects.all()  # Fetch all CPU data from your SQLite database
    return render(request, 'pc/gpu.html', {'Gpus': gpus})




def Motherboard_list_view(request):
    Motherboards = Motherboard.objects.all()  # Fetch all CPU data from your SQLite database
    return render(request, 'pc/motherboard.html', {'Motherboards':  Motherboards})

def RAM_list_view(request):
    Rams = Ram.objects.all()  # Fetch all CPU data from your SQLite database
    return render(request, 'pc/RAM.html', {'Rams':  Rams})


def Storage_list_view(request):
    Storages = Storage.objects.all()  # Fetch all CPU data from your SQLite database
    return render(request, 'pc/Storage.html', {'Storages': Storages})


def Powersupply_list_view(request):
    Power_supplys = PowerSupply.objects.all()  # Fetch all CPU data from your SQLite database
    return render(request, 'pc/Powersupply.html', {'Power_supplys': Power_supplys})

def Case_list_view(request):
    Cases = Case.objects.all()  # Fetch all CPU data from your SQLite database
    return render(request, 'pc/case.html', {'Cases': Cases})

def Monitor_list_view(request):
    Monitors = Monitor.objects.all()  # Fetch all CPU data from your SQLite database
    return render(request, 'pc/Monitor.html', {'Monitors': Monitors})

def OS_list_view(request):
    Operating_systems = OperatingSystem.objects.all()  # Fetch all CPU data from your SQLite database
    return render(request, 'pc/OS.html', {'Operating_systems': Operating_systems})


from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
from .models import PCBuild

def get_or_create_session_id(request):
    if not request.session.get('session_id'):
        request.session['session_id'] = get_random_string(32)  # Generate a unique session ID
    return request.session['session_id']



from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, redirect
from .models import PCBuild, CpuCooler, Motherboard, Ram, Storage, Case, PowerSupply, OperatingSystem, Monitor,CPU,GPU

def save_cpu_selection(request, cpu_id):
    session_id = get_or_create_session_id(request)
    selected_cpu = CPU.objects.get(id=cpu_id)
    
    # Get or create the PCBuild instance for this session
    pc_build, created = PCBuild.objects.get_or_create(session_id=session_id)
    pc_build.selected_cpu = selected_cpu.name  # Save the selected CPU name
    pc_build.save()
    
    return redirect('pc_build_summary')  # Redirect to a summary page or next component selection

def save_newcpu_selection(request,cpu_id):
    session_id= get_or_create_session_id(request)


def save_gpu_selection(request, gpu_id):
    session_id = get_or_create_session_id(request)
    selected_gpu = GPU.objects.get(id=gpu_id)
    
    pc_build, created = PCBuild.objects.get_or_create(session_id=session_id)
    pc_build.selected_gpu = selected_gpu.name
    pc_build.save()
    
    return redirect('pc_build_summary')

def save_Cpucooler_selection(request, cooler_id):
    session_id = get_or_create_session_id(request)
    selected_cpu_cooler = CpuCooler.objects.get(id=cooler_id)
    
    pc_build, created = PCBuild.objects.get_or_create(session_id=session_id)
    pc_build.selected_cpu_cooler= selected_cpu_cooler.name
    pc_build.save()
    
    return redirect('pc_build_summary')

def save_Monitor_selection(request, monitor_id):
    session_id = get_or_create_session_id(request)
    selected_monitor = Monitor.objects.get(id=monitor_id)
    
    pc_build, created = PCBuild.objects.get_or_create(session_id=session_id)
    pc_build.selected_monitor = selected_monitor.name
    pc_build.save()
    
    return redirect('pc_build_summary')

def save_motherboard_selection(request,motherboard_id):
    session_id = get_or_create_session_id(request)
    selected_motherboard= Motherboard.objects.get(id=motherboard_id)
    
    pc_build, created = PCBuild.objects.get_or_create(session_id=session_id)
    pc_build.selected_motherboard = selected_motherboard.name
    pc_build.save()
    
    return redirect('pc_build_summary')

def save_storage_selection(request,storage_id):
    session_id = get_or_create_session_id(request)
    selected_storage= Storage.objects.get(id=storage_id)
    
    pc_build, created = PCBuild.objects.get_or_create(session_id=session_id)
    pc_build.selected_storage = selected_storage.name
    pc_build.save()
    
    return redirect('pc_build_summary')

def save_ram_selection(request,ram_id):
    session_id = get_or_create_session_id(request)
    selected_ram= Ram.objects.get(id=ram_id)
    
    pc_build, created = PCBuild.objects.get_or_create(session_id=session_id)
    pc_build.selected_ram = selected_ram.name
    pc_build.save()
    
    return redirect('pc_build_summary')

def save_case_selection(request,case_id):
    session_id = get_or_create_session_id(request)
    selected_case= Case.objects.get(id=case_id)
    
    pc_build, created = PCBuild.objects.get_or_create(session_id=session_id)
    pc_build.selected_case = selected_case.name
    pc_build.save()
    
    return redirect('pc_build_summary')

def save_os_selection(request,os_id):
    session_id = get_or_create_session_id(request)
    selected_os= OperatingSystem.objects.get(id=os_id)
    
    pc_build, created = PCBuild.objects.get_or_create(session_id=session_id)
    pc_build.selected_os = selected_os.name
    pc_build.save()
    
    return redirect('pc_build_summary')

def save_psu_selection(request,psu_id):
    session_id = get_or_create_session_id(request)
    selected_psu= PowerSupply.objects.get(id=psu_id)
    
    pc_build, created = PCBuild.objects.get_or_create(session_id=session_id)
    pc_build.selected_psu = selected_psu.name
    pc_build.save()
    
    return redirect('pc_build_summary')

def convert_tdp_to_int(tdp_value):
    """Converts TDP from string format (like '250W') to integer."""
    if isinstance(tdp_value, str):
        # Remove the 'W' and convert the number to an integer
        return int(tdp_value.replace('W', '').strip())
    return tdp_value  # If it's already an integer, return as is

def recommend_cooling_system(total_tdp):
    """Returns a list of recommended coolers based on total TDP."""
    if total_tdp <= 250:
        # Recommend high-end air coolers for lower TDP
        recommended_coolers = [
            "Noctua NH-D15 (250W)",
            "Be Quiet! Dark Rock Pro 4 (250W)",
            "Corsair A500 (250W)"
        ]
    elif total_tdp <= 350:
        # Recommend premium air or entry-level liquid coolers
        recommended_coolers = [
            "Cooler Master ML240 (280W)",
            "Corsair H100i (250W)",
            "NZXT Kraken Z63 (280W)",
            "Thermaltake TH360 ARGB (360W)",
            "MSI MAG CoreLiquid 240R (280W)"
        ]
    elif total_tdp <= 500:
        # Recommend higher performance liquid coolers
        recommended_coolers = [
            "Thermaltake TH360 ARGB (360W)",
            "Cooler Master ML240 (280W)",
            "NZXT Kraken Z63 (280W)"
        ]
    else:
        # For very high TDP systems (500W-750W), recommend high-performance liquid coolers
        recommended_coolers = [
            "Thermaltake TH360 ARGB (360W)",
            "NZXT Kraken Z63 (280W)"
        ]
    
    return recommended_coolers


def calculate_performance_score(request):
    session_id = get_or_create_session_id(request)
    pc_build = PCBuild.objects.get(session_id=session_id)

    MAX_BENCHMARK = {
        'cpu': 108822,   # Max CPU benchmark score
        'gpu': 13959,    # Max GPU benchmark score
        'ram': 9500,
        'cpucoolers': 95,
        'Monitor': 950,
        'Mother board': 950,
        'OS': 930,
        'power supply': 970,
        'Storage': 8900,
        'case': 1080,
    }
    WEIGHTS = {
        'cpu': 0.20,
        'gpu': 0.20,
        'ram': 0.15,
        'psu': 0.05,
        'os': 0.05,
        'case': 0.05,
        'storage': 0.10,
        'motherboard': 0.10,
        'cpu_cooler': 0.05,
        'monitor': 0.05,
    }
    selected_cpu = CPU.objects.filter(name=pc_build.selected_cpu).first()
    selected_gpu = GPU.objects.filter(name=pc_build.selected_gpu).first()
    selected_ram = Ram.objects.filter(name=pc_build.selected_ram).first()
    selected_psu = PowerSupply.objects.filter(name=pc_build.selected_psu).first()
    selected_os = OperatingSystem.objects.filter(name=pc_build.selected_os).first()
    selected_case = Case.objects.filter(name=pc_build.selected_case).first()
    selected_storage = Storage.objects.filter(name=pc_build.selected_storage).first()
    selected_motherboard = Motherboard.objects.filter(name=pc_build.selected_motherboard).first()
    selected_cpu_cooler = CpuCooler.objects.filter(name=pc_build.selected_cpu_cooler).first()
    selected_monitor = Monitor.objects.filter(name=pc_build.selected_monitor).first()


    # Calculate individual scores
    new_cpu_score = (selected_cpu.cpu_mark / MAX_BENCHMARK['cpu']) if selected_cpu else 0
    new_gpu_score = ((selected_gpu.G3mark + selected_gpu.G2mark) / MAX_BENCHMARK['gpu']) if selected_gpu else 0
    new_ram_score = (selected_ram.benchmark / MAX_BENCHMARK['ram']) if selected_ram else 0
    new_psu_score = (selected_psu.benchmark / MAX_BENCHMARK['power supply']) if selected_psu else 0
    new_os_score = (selected_os.benchmark / MAX_BENCHMARK['OS']) if selected_os else 0
    new_case_score = (selected_case.benchmark / MAX_BENCHMARK['case']) if selected_case else 0
    new_storage_score = (selected_storage.benchmark / MAX_BENCHMARK['Storage']) if selected_storage else 0
    new_motherboard_score = (selected_motherboard.benchmark / MAX_BENCHMARK['Mother board']) if selected_motherboard else 0
    new_cpu_cooler_score = (selected_cpu_cooler.benchmark / MAX_BENCHMARK['cpucoolers']) if selected_cpu_cooler else 0
    new_monitor_score = (selected_monitor.benchmark / MAX_BENCHMARK['Monitor']) if selected_monitor else 0


    # Print individual scores to the console
#    # Print the weighted scores by multiplying with weights directly in the print statements
#     print("Weighted CPU Score:", (selected_cpu.cpu_mark / MAX_BENCHMARK['cpu']) * WEIGHTS['cpu'])
#     print("Weighted GPU Score:", (((selected_gpu.G3mark + selected_gpu.G2mark)/2) / MAX_BENCHMARK['gpu']) * WEIGHTS['gpu'])
#     print("Weighted RAM Score:", (selected_ram.benchmark / MAX_BENCHMARK['ram']) * WEIGHTS['ram'])
#     print("Weighted PSU Score:", (selected_psu.benchmark / MAX_BENCHMARK['power supply']) * WEIGHTS['psu'])
#     print("Weighted OS Score:", (selected_os.benchmark / MAX_BENCHMARK['OS']) * WEIGHTS['os'])
#     print("Weighted Case Score:", (selected_case.benchmark / MAX_BENCHMARK['case']) * WEIGHTS['case'])
#     print("Weighted Storage Score:", (selected_storage.benchmark / MAX_BENCHMARK['Storage']) * WEIGHTS['storage'])
#     print("Weighted Motherboard Score:", (selected_motherboard.benchmark / MAX_BENCHMARK['Mother board']) * WEIGHTS['motherboard'])
#     print("Weighted CPU Cooler Score:", (selected_cpu_cooler.benchmark / MAX_BENCHMARK['cpucoolers']) * WEIGHTS['cpu_cooler'])
#     print("Weighted Monitor Score:", (selected_monitor.benchmark / MAX_BENCHMARK['Monitor']) * WEIGHTS['monitor'])


    total_performance_score = ((
        new_cpu_score * WEIGHTS['cpu'] +
        new_gpu_score * WEIGHTS['gpu'] +
        new_ram_score * WEIGHTS['ram'] +
        new_psu_score * WEIGHTS['psu'] +
        new_os_score * WEIGHTS['os'] +
        new_case_score * WEIGHTS['case'] +
        new_storage_score * WEIGHTS['storage'] +
        new_motherboard_score * WEIGHTS['motherboard'] +
        new_cpu_cooler_score * WEIGHTS['cpu_cooler'] +
        new_monitor_score * WEIGHTS['monitor']
    )*100)


    total_tdp = (
        convert_tdp_to_int(selected_cpu.tdp) if selected_cpu else 0 +
        convert_tdp_to_int(selected_gpu.Tdp) if selected_gpu else 0 +
        convert_tdp_to_int(selected_cpu_cooler.tdp) if selected_cpu_cooler else 0
    )

    total_power = (
        convert_tdp_to_int(selected_cpu.tdp) if selected_cpu else 0 +
        convert_tdp_to_int(selected_gpu.Tdp) if selected_gpu else 0 +
        convert_tdp_to_int(selected_cpu_cooler.tdp) if selected_cpu_cooler else 0
    )

    cooling_recommendations = recommend_cooling_system(total_tdp)

    components = {
        'CPU': pc_build.selected_cpu,
        'GPU': pc_build.selected_gpu,
        'Motherboard': pc_build.selected_motherboard,
        'RAM': pc_build.selected_ram,
        'Storage': pc_build.selected_storage,
        'PSU': pc_build.selected_psu,
        'Case': pc_build.selected_case,
        'Monitor': pc_build.selected_monitor,
        'OS': pc_build.selected_os,
        'CPU Cooler': pc_build.selected_cpu_cooler
    }

    component_list = ", ".join([f"{key}: {value}" for key, value in components.items() if value])
    
    compatibility_report = check_compatibility_with_groq( component_list)

    if "not run"  in compatibility_report:
        total_performance_score =0
    
        
    return render(request, 'pc/summary.html', {
        'performance_score': total_performance_score,
        'pc_build': pc_build,
        'cooling_recommendations': cooling_recommendations,
        'total_power':total_power,
        'compatibility_report': compatibility_report,
        # Add the individual scores for debugging on the page
        'cpu_score': new_cpu_score,
        'gpu_score': new_gpu_score,
        'ram_score': new_ram_score,
        'psu_score': new_psu_score,
        'os_score': new_os_score,
        'case_score': new_case_score,
        'storage_score': new_storage_score,
        'motherboard_score': new_motherboard_score,
        'cpu_cooler_score': new_cpu_cooler_score,
        'monitor_score': new_monitor_score,
    })






def pc_build_summary(request):
    session_id = get_or_create_session_id(request)
    pc_build = PCBuild.objects.get(session_id=session_id)

   
    
    return render(request, 'pc/summary.html', {
        'pc_build': pc_build,
        
    })



def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")  # Redirect to login page after registration
    else:
        form = RegisterForm()
    return render(request, "pc/register.html", {"form": form})



def login_view(request):
    error = None
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            
            try:
                user = CustomUser.objects.get(email=email)
                if user.password == password:  # You can hash later
                    request.session['user_id'] = str(user.user_id)
                    return redirect("/")  # or your dashboard page
                else:
                    error = "Incorrect password."
            except CustomUser.DoesNotExist:
                error = "User does not exist."
    else:
        form = LoginForm()
    
    return render(request, "pc/login.html", {"form": form, "error": error})


# views.py
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from groq import Groq  # Make sure groq is installed and imported properly

@csrf_exempt
def get_pc_build_summary(request):
   try:
        session_id = request.session.get('session_id')
        pc_build = PCBuild.objects.get(session_id=session_id)
        
        if not pc_build:
            return "No PC build found."

        build_summary = f"""
        CPU: {pc_build.selected_cpu}
        GPU: {pc_build.selected_gpu}
        RAM: {pc_build.selected_ram}
        Storage: {pc_build.selected_storage}
        Motherboard: {pc_build.selected_motherboard}
        PSU: {pc_build.selected_psu}
        OS: {pc_build.selected_os}
        CPU Cooler: {pc_build.selected_cpu_cooler}
        Monitor: {pc_build.selected_monitor}
        Case: {pc_build.selected_case}
        """
        return build_summary.strip()
   except Exception as e:
        return f"Error retrieving build: {str(e)}"

def ask_bot(request):
    if request.method == "POST":
        data = json.loads(request.body)
        question = data.get("question", "")
        
        # Add your build info, DB info, and site info here
        website_info = "This is a PC Picker tool where users can choose compatible parts and get performance & power insights."

        user_id = request.session.get("user_id")

       
        build_info = get_pc_build_summary(user_id)
        
        
        full_prompt = f"{website_info}\n\n{build_info}\n\n User Question: {question}"


        try:
            client = Groq(api_key="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")
            response = client.chat.completions.create(
                messages=[{"role": "user", "content": full_prompt}],
                model="llama3-8b-8192",
                temperature=0.01,
            )
            answer = response.choices[0].message.content
            return JsonResponse({"answer": answer})
        except Exception as e:
            return JsonResponse({"answer": "Error: " + str(e)}, status=500)
def save_build(request):
    session_id = get_or_create_session_id(request)
    pc_build = PCBuild.objects.get(session_id=session_id)

    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')  # if not logged in

    build_name = request.POST.get('build_name')  # <-- get the build name from the form

    SaveBuild.objects.create(
        user_id=user_id,
        build_name=build_name,  # <-- save the entered name here
        selected_cpu=pc_build.selected_cpu,
        selected_gpu=pc_build.selected_gpu,
        selected_motherboard=pc_build.selected_motherboard,
        selected_ram=pc_build.selected_ram,
        selected_storage=pc_build.selected_storage,
        selected_psu=pc_build.selected_psu,
        selected_case=pc_build.selected_case,
        selected_monitor=pc_build.selected_monitor,
        selected_os=pc_build.selected_os,
        selected_cpu_cooler=pc_build.selected_cpu_cooler,
        
    )

    return redirect('view_builds')

def view_builds(request):
    user_id = request.session.get('user_id')
    
    if not user_id:
        return redirect('login')  # Force login if user not logged in

    saved_builds = SaveBuild.objects.filter(user_id=user_id)  # Get all builds saved by this user
    
    return render(request, 'pc/savebuild.html', {'saved_builds': saved_builds})

def load_build(request,build_id):
    saved_build = SaveBuild.objects.get(id=build_id)

    return render(request, 'pc/summary.html', {
        'pc_build': saved_build,
        
    })
from .models import SaveBuild

def get_saved_build_context(user_id):
    try:
        saved = SaveBuild.objects.filter(user_id=user_id).last()
        if not saved:
            return "No saved build found."

        context_lines = [
            f"Build Name: {saved.build_name}",
            f"CPU: {saved.selected_cpu}",
            f"GPU: {saved.selected_gpu}",
            f"RAM: {saved.selected_ram}",
            f"Storage: {saved.selected_storage}",
            f"Motherboard: {saved.selected_motherboard}",
            f"PSU: {saved.selected_psu}",
            f"OS: {saved.selected_os}",
            f"CPU Cooler: {saved.selected_cpu_cooler}",
            f"Monitor: {saved.selected_monitor}",
            f"Case: {saved.selected_case}",
        ]
        return "\n".join(context_lines)

    except Exception as e:
        return f"Error retrieving saved build: {str(e)}"


from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from rag_ask import get_ollama_answer

@csrf_exempt
def ask_bot_ollama(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            query = data.get("question", "")
            user_id = request.session.get('user_id')
              
            answer = get_ollama_answer(query)
            return JsonResponse({"answer": answer})
        except Exception as e:
            return JsonResponse({"answer": f"Error: {str(e)}"}, status=500)

def get_live_cpu(request):
    cpus = Live_CPU.objects.all()
    data = []
    for cpu in cpus:
        data.append({
            
            'name': cpu.name,
            'cpu_mark': cpu.cpu_mark,
            'tdp': cpu.tdp,
            'socket': cpu.socket,
            'cores': cpu.cores,
        })
    return JsonResponse({'cpus': data})
def get_normal_cpu(request):
    cpus= CPU.objects.all()
    data=[]
    for cpu in cpus:
         data.append({
            
            'name': cpu.name,
            'cpu_mark': cpu.cpu_mark,
            'tdp': cpu.tdp,
            'socket': cpu.socket,
            'cores': cpu.cores,
        })
    return JsonResponse({'cpus': data})
