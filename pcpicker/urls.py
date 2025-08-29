from django.urls import path
from . import views 


urlpatterns = [
    path('', views.index_view, name='index'),  
    path('cpu/', views.cpu_list_view, name='cpu'),
    path('gpu/', views.gpu_list_view, name='gpu'),
    path('cpucooler/', views.cpucooler_list_view, name='Cpucooler'),
    path('motherboard/', views.Motherboard_list_view, name='Motherboards'),
    path('Monitor/', views.Monitor_list_view, name='Monitors'),
    path('case/', views.Case_list_view, name='Cases'),
    path('OS/', views.OS_list_view, name='Operating_systems'),
    path('Powersupply/', views.Powersupply_list_view, name='Power_supplys'),
    path('Storage/', views.Storage_list_view, name='Storages'),
    path('RAM/', views.RAM_list_view, name='Rams'),


    path('save_cpu/<int:cpu_id>/', views.save_cpu_selection, name='save_cpu_selection'),
    path('save_gpu/<int:gpu_id>/', views.save_gpu_selection, name='save_gpu_selection'),
    path('save_Cpucooler/<int:cooler_id>/', views.save_Cpucooler_selection, name='save_cpu_cooler'),
    path('save_Monitor/<int:monitor_id>/', views.save_Monitor_selection, name='save_Monitor'),
    path('save_motherboard/<int:motherboard_id>/', views.save_motherboard_selection, name='save_motherboard'),
    path('save_storage/<int:storage_id>/', views.save_storage_selection, name='save_storage'),
    path('save_ram/<int:ram_id>/', views.save_ram_selection, name='save_ram'),
    path('save_case/<int:case_id>/', views.save_case_selection, name='save_case'),
    path('save_os/<int:os_id>/', views.save_os_selection, name='save_os'),
    path('save_psu/<int:psu_id>/', views.save_psu_selection, name='save_psu'),
    path('pc_build_summary/', views.pc_build_summary, name='pc_build_summary'),
    path('summary/', views.calculate_performance_score, name='pc_build_summary'),
    path("register/",views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("ask/", views.ask_bot, name="ask_bot"),
    path('SaveBuild/', views.save_build, name='save_build'),
    path('ViewBuild/', views.view_builds, name='view_builds'),
    path(' loadbuild/<int:build_id>', views.load_build, name='load_build'),
    path("ask_ollama/", views.ask_bot_ollama, name="ask_bot_ollama"),
    path("get_live_cpu/",views.get_live_cpu,name='get_live_cpu'),
    path("get_normal_cpu/",views.get_normal_cpu,name='get_normal_cpu')
   
    

]    

