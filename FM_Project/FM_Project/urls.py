"""FM_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from FM_App import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.loginpage,name="homepage"),
    path('usernamecheck/',views.usernamecheck,name="usernamecheck"),
    path('passwordcheck/',views.passwordcheck,name="passwordcheck"),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('finduser/',views.finduser,name="finduser"),
    path('getadminpwd/',views.getadminpwd,name="getadminpwd"),
    path('check_username_Exist/',views.check_username_Exist,name="check_username_Exist"),
    path('check_checkempid_Exist/',views.check_checkempid_Exist,name="check_checkempid_Exist"),
    path('savedata/',views.savedata,name="savedata"),
    path('fetch_usernames_and_ids/', views.fetch_usernames_and_ids, name='fetch_usernames_and_ids'),
    path('check_fpassword/', views.check_password_for_employee, name='check_fpassword'),
    path('usernamecheckvalue/', views.usernamecheckvalue, name='usernamecheckvalue'),
    path('employeeidcheck/', views.employeeidcheck, name='employeeidcheck'),
    # path('resourcemgnt/',views.resourcemgnt,name="resourcemgnt"),
    path('add_valve/',views.add_valve,name="add_valve"),
    path('add_valveclass/',views.add_valveclass,name="add_valveclass"),
    path('add_valvetype/',views.add_valvetype,name="add_valvetype"),
    path('add_flagedtype/',views.add_flagedtype,name="add_flagedtype"),
    path('add_actuatortype/',views.add_actuatortype,name="add_actuatortype"),
    path('add_unittype/',views.add_unittype,name="add_unittype"),
    path('get_valve_size/<int:valve_size_id>/', views.get_valve_size, name='get_valve_size'),
    path('update_valve_size/', views.update_valve_size, name='update_valve_size'),
    path('delete_valve/', views.delete_valve, name='delete_valve'),
    path('get_valve_class/<int:classid>/', views.get_valve_class, name='get_valve_class'),
    path('update_valve_class/', views.update_valve_class, name='update_valve_class'),
    path('delete_valveclass/', views.delete_valveclass, name='delete_valveclass'),
    path('get_valve_type/<int:typeid>/', views.get_valve_type, name='get_valve_type'),
    path('update_valve_type/', views.update_valve_type, name='update_valve_type'),
    path('delete_valvetype/', views.delete_valvetype, name='delete_valvetype'),
    path('get_flang_type/<int:flagid>/', views.get_flang_type, name='get_flang_type'),
    path('update_flang_type/', views.update_flang_type, name='update_flang_type'),
    path('delete_flangtype/', views.delete_flangtype, name='delete_flangtype'),
    path('get_actuator_type/<int:actuatorid>/', views.get_actuator_type, name='get_actuator_type'),
    path('update_actuator_type/', views.update_actuator_type, name='update_actuator_type'),
    path('delete_actuatortype/', views.delete_actuatortype, name='delete_actuatortype'),
    path('get_unit_type/<int:unitid>/', views.get_unit_type, name='get_unit_type'),
    path('update_unit_type/', views.update_unit_type, name='update_unit_type'),
    path('delete_unittype/', views.deleteunittype, name='delete_unittype'),
    
    path('crud',views.crud),
    path('addnameandage/',views.addnameandage),
    path('getrecord/<int:id>/', views.getrecord, name='getrecord'),
    path('updaterecord/<int:id>/', views.updaterecord, name='updaterecord'),
    path('deleterecord/<int:id>/', views.deleterecord, name='delete_data'),
    path('get_data/<int:productid>/',views.get_data),
    path('updatedata/<int:productid>/',views.updatedata),
    path('deletegrid/<int:productid>/',views.deletegrid),
    path('settings/',views.settings),
    path('save_setting_data/',views.savesetting),
    path('recentlogin/',views.recent_login),
    # path('save_hmi_details'.views.save_hmi_details),
    path('tasks',views.tasks),
    path('livestatus',views.livestatus),
    path('users',views.users),
    path('savedata1',views.savedata1),
    path('edit_data/<int:id>/',views.edit_data),
    path('update/',views.update),
    
    path('resourcemgnt/',views.resourcemgnt),
    path('savevalvedata/',views.savevalvedata),
    path('deletedata/',views.deletedata),
    path('get_data_for_edit/',views.get_data_for_edit),
    path('save_updateddata/',views.save_updateddata),
    path('save_classtype/',views.save_classtype),
    path('get_update_classtype/',views.get_update_classtype),
    path('save_editedclasstype/',views.save_editedclasstype),
    path('delete_valvetype/',views.delete_valvetype),
    path('save_valveclass/',views.save_valveclass),
    path('fetch_classdata/',views.fetch_classdata),
    path('save_updatedclass/',views.save_updatedclass),
    path('save_flangeddata/',views.save_flangeddata),
    path('fetch_flangdata/',views.fetch_flangdata),
    path('save_updatedflang/',views.save_updatedflang),
    path('save_actuator/',views.save_actuator),
    path('getvalue_forupdate/',views.getvalue_forupdate),
    path('save_updated_actuator/',views.save_updated_actuator),
    path('delete_actuator/',views.delete_actuator),
    path('save_unit/',views.save_unit),
    path('getunit_forupdate/',views.getunit_forupdate),
    path('save_updated_unit/',views.save_updated_unit),
    path('delete_unit/',views.delete_unit),
    path('save_product/',views.save_product,name="save_product"),
    path('get_product_forupdate/',views.get_product_forupdate),
    path('save_updatedproduct/',views.save_updatedproduct),
    path('delete_product/',views.delete_product),
    path('logout/', views.logout_view, name='logout'),
] 
