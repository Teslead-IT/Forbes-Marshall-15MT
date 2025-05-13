from pyexpat.errors import messages
from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.db import connection,IntegrityError
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password 
import json
import logging
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login,logout


# Create your views here.
def loginpage(request):
    
    with connection.cursor() as cursor:
        cursor.execute("select username,employee_id from fm_R12 ORDER BY username ASC")
        val = cursor.fetchall()
          
   
    return render(request,"loginpage.html",{"value":val})

# @login_required
# @csrf_exempt
# def resourcemgnt(request):
#     with connection.cursor() as cursor:
#         cursor.execute("select * from valve_size")
#         valve_size = cursor.fetchall()
               
#     valve_size_data = [
#         {"column1": row[0], "column2": row[1], "column3": row[2]}
#         for row in valve_size
#     ]
    
#     with connection.cursor() as cursor:
#         cursor.execute("select * from valve_class")
#         valve_class = cursor.fetchall()
        
#     valve_class_data = [
#         {"column4": row1[0], "column5": row1[1], "column6": row1[2]}
#         for row1 in valve_class
#     ]  
#     print(valve_class_data)
    
#     with connection.cursor() as cursor:
#         cursor.execute("select * from valve_type")
#         valve_type = cursor.fetchall()
        
#     valve_type_data = [
#         {"column7": row2[0], "column8": row2[1], "column9": row2[2]}
#         for row2 in valve_type
#     ] 
    
#     with connection.cursor() as cursor:
#         cursor.execute("select * from valve_flanged")
#         valve_flanged = cursor.fetchall()
        
#     valve_flanged_data = [
#         {"column10": row3[0], "column11": row3[1], "column12": row3[2]}
#         for row3 in valve_flanged
#     ]
    
#     with connection.cursor() as cursor:
#         cursor.execute("select * from valve_actuator")
#         valve_actuator = cursor.fetchall()
        
#     valve_actuator_data = [
#         {"column13": row4[0], "column14": row4[1], "column15": row4[2]}
#         for row4 in valve_actuator
#     ] 
    
#     with connection.cursor() as cursor:
#         cursor.execute("select * from valve_unit")
#         valve_unit = cursor.fetchall()
        
#     valve_unit_data = [
#         {"column16": row5[0], "column17": row5[1], "column18": row5[2]}
#         for row5 in valve_unit
#     ]
    
#     with connection.cursor() as cursor:
#         cursor.execute("select * from add_product")
#         product = cursor.fetchall()
        
#     product_detail=[
#         {"row1":row[1], "row2":row[2], "row3":row[3],"row4":row[4]}
#         for row in product
#     ]
        
    
#     return render(request,"resourcemgnt.html",{"valve_size_data":valve_size_data,"valve_class_data":valve_class_data,"valve_type_data":valve_type_data,"valve_flanged_data":valve_flanged_data,"valve_actuator_data":valve_actuator_data,"valve_unit_data":valve_unit_data,"product_detail":product_detail})

@csrf_exempt
def usernamecheck(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        
        with connection.cursor() as cursor:
            cursor.execute("select username from fm_project where username=%s",[username])
            value = cursor.fetchone()
            
            if value:               
                return JsonResponse({"status": "success"})
            else:
                return JsonResponse({"status": "failure", "message": "No username found"})
    else:
        return JsonResponse({"status": "failure", "message": "Invalid request method"})

    
# Set up logging
logger = logging.getLogger(__name__)

# @csrf_exempt
# def usernamecheck(request):
#     if request.method == 'POST':
#         try:
#             data = json.loads(request.body)  
#             username = data.get('username')  # Extract username from the data
#             logger.debug(f"Received username: {username}")
            
#             with connection.cursor() as cursor:
#                 cursor.execute("SELECT username FROM fm_project WHERE username=%s", [username])
#                 value = cursor.fetchone()
                
#                 logger.debug(f"Database query result: {value}")
                
#                 if value:
#                     return JsonResponse({"status": "exists"})
#                 else:
#                     return JsonResponse({"status": "not_exists", "message": "Username not found"})
        
#         except json.JSONDecodeError:
#             logger.error("Invalid JSON format in request body")
#             return JsonResponse({"status": "failure", "message": "Invalid JSON format"})
    
#     return JsonResponse({"status": "failure", "message": "Invalid request method"})

@csrf_exempt
def passwordcheck(request):
    if request.method == "POST":
        password = request.POST.get("password")
        
        with connection.cursor() as cursor:
            # Get the username, employee_id, and password from the database
            cursor.execute("SELECT username, employee_id, password,is_superuser FROM fm_project WHERE password=%s", [password])
            value1 = cursor.fetchone()
            
            if value1:
                username = value1[0]
                employee_id = value1[1]
                is_superuser = value1[3]
                
                user, created = User.objects.get_or_create(username=username, defaults={
                    'is_superuser': is_superuser,
                    'is_staff': is_superuser,
                    'password': '!'  # Mark as unusable password
                })

                login(request, user)
                        
                request.session["superuser"]=is_superuser
                
                print("superuser",is_superuser)
                # Check if the employee_id already exists in the recent_login table
                cursor.execute("SELECT * FROM recent_login WHERE employee_id=%s", [employee_id])
                existing_record = cursor.fetchone()

                if existing_record:
                    # If the record exists, update the current_datetime to NOW()
                    cursor.execute("""
                        UPDATE recent_login
                        SET current_datetime = NOW()
                        WHERE employee_id = %s
                    """, [employee_id])
                else:
                    # If the record doesn't exist, insert a new record with the current time
                    cursor.execute("""
                        INSERT INTO recent_login (username, employee_id, current_datetime)
                        VALUES (%s, %s, NOW())
                    """, [username, employee_id])
                
                # Remove records that are older than 1 hour from recent_login table
                cursor.execute("""
                    DELETE FROM recent_login
                    WHERE current_datetime < NOW() - INTERVAL 1 HOUR
                """)
                connection.commit()
            
                
                return JsonResponse({"status": "success","superuser":is_superuser,"redirect_url": "/dashboard"})
            else:
                return JsonResponse({"status": "failure", "message": "No password found"})
    else:
        return JsonResponse({"status": "failure", "message": "Invalid request method"})

       

@csrf_exempt
def finduser(request):
    if request.method == "POST":
        employeeid = request.POST.get("employeeid")
        
        with connection.cursor() as cursor:
            cursor.execute("select username from fm_project where employee_id = %s",[employeeid])
            value2 = cursor.fetchone()
        if value2:
            return JsonResponse({"status":"success","message":"username found","emp_id":value2[0]})
        else:
            return JsonResponse({"status":"failure","message":"username not found"})
    return JsonResponse({"status": "failure", "message": "Invalid request method"})

@csrf_exempt
def getadminpwd(request):
    if request.method == "POST":
        adminpassword = request.POST.get("adminpassword")
        with connection.cursor() as cursor:
            # cursor.execute("select password from fm_project where password=%s and is_superuser=%s", [adminpassword, True])
            cursor.execute("SELECT password, is_superuser FROM fm.fm_project WHERE password = %s",[adminpassword])
            value3 = cursor.fetchone()
            if value3:
                return JsonResponse({"status":"success"})
            else:
                return JsonResponse({"status":"failure","message":"password not found"})
    return JsonResponse({"status": "failure", "message": "Invalid request method"})


@csrf_exempt
def check_username_Exist(request):
    if request.method == "POST":
        checkusername1 = request.POST.get("checkusername")
        
        with connection.cursor() as cursor:
            cursor.execute("select username from fm_project where username=%s",[checkusername1])
            value4 = cursor.fetchone()
            if value4:
                return JsonResponse({"status":"success","message":"Username found"})
            else:
                return JsonResponse({"status":"failure","message":"Username not found"})
    return JsonResponse({"status": "failure", "message": "Invalid request method"})

@csrf_exempt
def check_checkempid_Exist(request):
    if request.method == "POST":
        checkemployeeid = request.POST.get("checkemp_id")
        with connection.cursor() as cursor:
            cursor.execute("select employee_id from fm_project where employee_id = %s",[checkemployeeid])
            value5 = cursor.fetchone()
            if value5:
                return JsonResponse({"status":"success","message":"Employee id found"})
            else:
                return JsonResponse({"status":"failure","message":"Employee not found"})
    return JsonResponse({"status": "failure", "message": "Invalid request method"})

@csrf_exempt
def savedata(request):
    if request.method == "POST":
        firstname1 = request.POST.get("firstname")
        lastname1 = request.POST.get("lastname")
        usernamevalue1 = request.POST.get("usernamevalue")
        checkemp_id = request.POST.get("checkempid1")
        password1 = request.POST.get("password1")
        with connection.cursor() as cursor:
            cursor.execute("""
        INSERT INTO fm_project (username, password, first_name, last_name, employee_id,login_time) 
        VALUES (%s, %s, %s, %s, %s,NOW())
    """, [usernamevalue1, password1, firstname1, lastname1, checkemp_id])
            
        return JsonResponse({
            "status": "success",
            "message": "Data added successfully",
            "username": usernamevalue1, 
            "employee_id": checkemp_id 
        })
        
    return JsonResponse()

def fetch_usernames_and_ids(request):
    # Open a database connection and execute the raw SQL query
    with connection.cursor() as cursor:
        cursor.execute("SELECT username, employee_id FROM fm_project ORDER BY username ASC")
        users = cursor.fetchall()

    # Prepare the result to be sent as JSON
    users_data = [{"username": user[0], "employee_id": user[1]} for user in users]

    return JsonResponse({"status": "success", "data": users_data})
    
@csrf_exempt
def check_password_for_employee(request):
    if request.method == 'POST':
        employee_id = request.POST.get('employee_id')
        fpassword = request.POST.get('fpassword')
        
        print(fpassword)  # Debugging step
        
        # Query the user by employee_id from the database
        with connection.cursor() as cursor:
            cursor.execute("SELECT password FROM fm_R12 WHERE employee_id = %s", [employee_id])
            user = cursor.fetchone()

        if user:
            # The password is stored as a hashed value in the database
            stored_password = user[0]  # The first column is the password (not the second)
            print({"storedpwd": stored_password})  # Debugging step

            # Check if the entered password matches the stored password (hashed)
            if fpassword == stored_password:
                 return JsonResponse({"status": "success", "message": "Password is correct"})
            else:
                return JsonResponse({"status": "error", "message": "Invalid password"})
        else:
            return JsonResponse({"status": "error", "message": "User not found"})

    return JsonResponse({"status": "error", "message": "Invalid request"})


@csrf_exempt
def usernamecheckvalue(request):
   if request.method == 'POST':
        try:
            data = json.loads(request.body)  
            username = data.get('username')  # Extract username from the data
            logger.debug(f"Received username: {username}")
            
            with connection.cursor() as cursor:
                cursor.execute("SELECT username FROM fm_project WHERE username=%s", [username])
                value = cursor.fetchone()
                
                logger.debug(f"Database query result: {value}")
                
                if value:
                    return JsonResponse({"status": "exists"})
                else:
                    return JsonResponse({"status": "not_exists", "message": "Username not found"})
        
        except json.JSONDecodeError:
            logger.error("Invalid JSON format in request body")
            return JsonResponse({"status": "failure", "message": "Invalid JSON format"})
    
        return JsonResponse({"status": "failure", "message": "Invalid request method"})
    
@csrf_exempt
def employeeidcheck(request):
   if request.method == 'POST':
        try:
            data = json.loads(request.body)  
            employeeid = data.get('employeeid')  # Extract username from the data
            logger.debug(f"Received username: {employeeid}")
            
            with connection.cursor() as cursor:
                cursor.execute("SELECT employee_id FROM fm_project WHERE employee_id=%s", [employeeid])
                value = cursor.fetchone()
                
                logger.debug(f"Database query result: {value}")
                
                if value:
                    return JsonResponse({"status": "exists"})
                else:
                    return JsonResponse({"status": "not_exists", "message": "Username not found"})
        
        except json.JSONDecodeError:
            logger.error("Invalid JSON format in request body")
            return JsonResponse({"status": "failure", "message": "Invalid JSON format"})
    
        return JsonResponse({"status": "failure", "message": "Invalid request method"})

# @csrf_exempt
# def add_valve(request):
#     if request.method == "POST":
#         valvesizeid=request.POST.get("valve_size_id")
#         valvesizename=request.POST.get("valve_size_name")
#         valvesizedescription=request.POST.get("valve_size_description")
        
#         print(valvesizeid)
#         print(valvesizename) 
#         print(valvesizedescription)
        
#         with connection.cursor() as cursor:
#             cursor.execute("insert into valve_size (valve_size_id,valve_size_name,valve_size_description) values (%s,%s,%s)",[valvesizeid,valvesizename,valvesizedescription])
    
#             return JsonResponse({'status':'success','message':'Data added'})
#     else:
#         return JsonResponse({'status':'failure','message':'Data not added'})
            
#     return JsonResponse({"status": "error", "message": "Invalid request"})

@csrf_exempt
def add_valve(request):
    if request.method == "POST":
        valveid=request.POST.get("valveid")
        valvename=request.POST.get("valvename")
        valvedes=request.POST.get("valvedes")
        
        with connection.cursor() as cursor:
            cursor.execute("insert into valve_size (valve_size_id,valve_size_name,valve_size_description) values (%s,%s,%s)",[valveid,valvename,valvedes])
    
            return JsonResponse({'status':'success','message':'Data added'})
    else:
        return JsonResponse({'status':'failure','message':'Data not added'})
            
    return JsonResponse({"status": "error", "message": "Invalid request"})

@csrf_exempt
def add_valveclass(request):
    if request.method == "POST":
        classid=request.POST.get("classid")
        classname=request.POST.get("classname")
        classdes=request.POST.get("classdes")
        
        with connection.cursor() as cursor:
            cursor.execute("insert into valve_class (valve_class_id,valve_class_name,valve_class_description) values (%s,%s,%s)",[classid,classname,classdes])
    
            return JsonResponse({'status':'success','message':'Data added'})
    else:
        return JsonResponse({'status':'failure','message':'Data not added'})
            
    return JsonResponse({"status": "error", "message": "Invalid request"})

@csrf_exempt
def add_valvetype(request):
    if request.method == "POST":
        typeid=request.POST.get("typeid")
        typename=request.POST.get("typename")
        typedesc=request.POST.get("typedesc")
         
        with connection.cursor() as cursor:
            cursor.execute("insert into valve_type (valve_type_id,valve_type_name,valve_type_description) values (%s,%s,%s)",[typeid,typename,typedesc])
    
            return JsonResponse({'status':'success','message':'Data added'})
    else:
        return JsonResponse({'status':'failure','message':'Data not added'})
            
    return JsonResponse({"status": "error", "message": "Invalid request"})

@csrf_exempt
def add_flagedtype(request):
    if request.method == "POST":
        flagid=request.POST.get("flagid")
        flagname=request.POST.get("flagname")
        flagdesc=request.POST.get("flagdesc")
         
        with connection.cursor() as cursor:
            cursor.execute("insert into valve_flanged (flanged_type_id,flanged_type_name,flanged_type_description) values (%s,%s,%s)",[flagid,flagname,flagdesc])
    
            return JsonResponse({'status':'success','message':'Data added'})
    else:
        return JsonResponse({'status':'failure','message':'Data not added'})
            
    return JsonResponse({"status": "error", "message": "Invalid request"})

@csrf_exempt
def add_actuatortype(request):
    if request.method == "POST":
        actuatorid=request.POST.get("actuatorid")
        actuatorname=request.POST.get("actuatorname")
        actuatordesc=request.POST.get("actuatordesc")
         
        with connection.cursor() as cursor:
            cursor.execute("insert into valve_actuator (actuator_type_id,actuator_type_name,actuator_type_description) values (%s,%s,%s)",[actuatorid,actuatorname,actuatordesc])
    
            return JsonResponse({'status':'success','message':'Data added'})
    else:
        return JsonResponse({'status':'failure','message':'Data not added'})
            
    return JsonResponse({"status": "error", "message": "Invalid request"})

@csrf_exempt
def add_unittype(request):
    if request.method == "POST":
        unitid=request.POST.get("unitid")
        unitname=request.POST.get("unitname")
        unitdes=request.POST.get("unitdes")
         
        with connection.cursor() as cursor:
            cursor.execute("insert into valve_unit (unit_id,unit_name,unit_description) values (%s,%s,%s)",[unitid,unitname,unitdes])
    
            return JsonResponse({'status':'success','message':'Data added'})
    else:
        return JsonResponse({'status':'failure','message':'Data not added'})
            
    return JsonResponse({"status": "error", "message": "Invalid request"})



#  Edit valve size

def get_valve_size(request, valve_size_id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM valve_size WHERE valve_size_id = %s", [valve_size_id])
        row = cursor.fetchone()
    
    if row:
        valve_size_data = {
            'valve_size_id': row[0],
            'valve_size_name': row[1],
            'valve_size_description': row[2]
        }
        return JsonResponse(valve_size_data)
    else:
        return JsonResponse({'error': 'Valve size not found'}, status=404)

# View to update valve size
@csrf_exempt
def update_valve_size(request):
    if request.method == "POST":
        valvename = request.POST.get('valvename')
        valvedes = request.POST.get('valvedes')
        valvesize = request.POST.get('valvesize')

        if not valvesize:
            return JsonResponse({'status': 'failure', 'message': 'Missing valve size ID for update'})

        # Make sure you're updating the existing record, not inserting a new one
        with connection.cursor() as cursor:
            cursor.execute("""
                UPDATE valve_size 
                SET valve_size_name = %s, valve_size_description = %s 
                WHERE valve_size_id = %s
            """, [valvename, valvedes, valvesize])

        return JsonResponse({'status': 'success', 'message': 'Valve size updated successfully'})
    else:
        return JsonResponse({'status': 'failure', 'message': 'Invalid request'})


@csrf_exempt
def delete_valve(request):
    if request.method == 'POST':
        try:
            # Get the data from the request body
            data = json.loads(request.body)
            valve_size_id = data.get('valve_size_id')
            
            # Delete the valve size from the database
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM valve_size WHERE valve_size_id = %s", [valve_size_id])

            return JsonResponse({'status': 'success', 'message': 'Valve size deleted successfully'})
        except Exception as e:
            return JsonResponse({'status': 'failure', 'message': str(e)})

    return JsonResponse({'status': 'failure', 'message': 'Invalid request'})


#  Edit valve class

def get_valve_class(request, classid):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM valve_class WHERE valve_class_id = %s", [classid])
        row = cursor.fetchone()
    
    if row:
        valve_class_data = {
            'valve_class_id': row[0],
            'valve_class_name': row[1],
            'valve_class_description': row[2]
        }
        return JsonResponse(valve_class_data)
    else:
        return JsonResponse({'error': 'Valve class not found'}, status=404)


# View to update valve size
@csrf_exempt
def update_valve_class(request):
    if request.method == "POST":
        classid = request.POST.get('classid')
        classname = request.POST.get('classname')
        classdes = request.POST.get('classdes')
        current_valve_class_id = request.POST.get('current_valve_class_id')

        with connection.cursor() as cursor:
            cursor.execute("""
                UPDATE valve_class 
                SET valve_class_name = %s, valve_class_description = %s 
                WHERE valve_class_id = %s
            """, [classname, classdes, current_valve_class_id])

        return JsonResponse({'status': 'success', 'message': 'Valve class updated successfully'})
    else:
        return JsonResponse({'status': 'failure', 'message': 'Invalid request'})
    

@csrf_exempt
def delete_valveclass(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            classid = data.get('classid')

            # Delete from the database
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM valve_class WHERE valve_class_id = %s", [classid])

            return JsonResponse({'status': 'success', 'message': 'Valve class deleted successfully'})
        except Exception as e:
            return JsonResponse({'status': 'failure', 'message': str(e)})

    return JsonResponse({'status': 'failure', 'message': 'Invalid request'})

#  Edit valve type

def get_valve_type(request, typeid):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM valve_type WHERE valve_type_id = %s", [typeid])
        row = cursor.fetchone()
    
    if row:
        valve_type_data = {
            'valve_type_id': row[0],
            'valve_type_name': row[1],
            'valve_type_description': row[2]
        }
        return JsonResponse(valve_type_data)
    else:
        return JsonResponse({'error': 'Valve type not found'}, status=404)


# View to update valve size
@csrf_exempt
def update_valve_type(request):
    if request.method == "POST":
        typeid = request.POST.get('typeid')
        typename = request.POST.get('typename')
        typedesc = request.POST.get('typedesc')
        current_valve_type_id = request.POST.get('current_valve_type_id')

        with connection.cursor() as cursor:
            cursor.execute("""
                UPDATE valve_type
                SET valve_type_name = %s, valve_type_description = %s 
                WHERE valve_type_id = %s
            """, [ typename,typedesc, current_valve_type_id])

        return JsonResponse({'status': 'success', 'message': 'Valve type updated successfully'})
    else:
        return JsonResponse({'status': 'failure', 'message': 'Invalid request'})
    

@csrf_exempt
def delete_valvetype(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            typeid = data.get('typeid')

            # Delete from the database
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM valve_type WHERE valve_type_id = %s", [typeid])

            return JsonResponse({'status': 'success', 'message': 'Valve type deleted successfully'})
        except Exception as e:
            return JsonResponse({'status': 'failure', 'message': str(e)})

    return JsonResponse({'status': 'failure', 'message': 'Invalid request'})


#  Edit flang type

def get_flang_type(request, flagid):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM valve_flanged WHERE flanged_type_id = %s", [flagid])
        row = cursor.fetchone()
    
    if row:
        flanged_type_data = {
            'flanged_type_id': row[0],
            'flanged_type_name': row[1],
            'flanged_type_description': row[2]
        }
        return JsonResponse(flanged_type_data)
    else:
        return JsonResponse({'error': 'flanged type not found'}, status=404)


# View to update valve size
@csrf_exempt
def update_flang_type(request):
    if request.method == "POST":
        flagid = request.POST.get('flagid')
        flagname = request.POST.get('flagname')
        flagdesc = request.POST.get('flagdesc')
        current_flang_type_id = request.POST.get('current_flang_type_id')

        with connection.cursor() as cursor:
            cursor.execute("""
                UPDATE valve_flanged
                SET flanged_type_name = %s, flanged_type_description = %s 
                WHERE flanged_type_id = %s
            """, [ flagname,flagdesc, current_flang_type_id])

        return JsonResponse({'status': 'success', 'message': 'flang type updated successfully'})
    else:
        return JsonResponse({'status': 'failure', 'message': 'Invalid request'})
    


#  Edit flang type

def get_flang_type(request, flagid):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM valve_flanged WHERE flanged_type_id = %s", [flagid])
        row = cursor.fetchone()
    
    if row:
        flanged_type_data = {
            'flanged_type_id': row[0],
            'flanged_type_name': row[1],
            'flanged_type_description': row[2]
        }
        return JsonResponse(flanged_type_data)
    else:
        return JsonResponse({'error': 'flanged type not found'}, status=404)


# View to update valve size
@csrf_exempt
def update_flang_type(request):
    if request.method == "POST":
        flagid = request.POST.get('flagid')
        flagname = request.POST.get('flagname')
        flagdesc = request.POST.get('flagdesc')
        current_flang_type_id = request.POST.get('current_flang_type_id')

        with connection.cursor() as cursor:
            cursor.execute("""
                UPDATE valve_flanged
                SET flanged_type_name = %s, flanged_type_description = %s 
                WHERE flanged_type_id = %s
            """, [ flagname,flagdesc, current_flang_type_id])

        return JsonResponse({'status': 'success', 'message': 'flang type updated successfully'})
    else:
        return JsonResponse({'status': 'failure', 'message': 'Invalid request'})
    

@csrf_exempt
def delete_flangtype(request):
    if request.method == 'POST':
        try:
            flagid = request.POST.get('id')

            if(flagid):
            # Delete from the database
                with connection.cursor() as cursor:
                    cursor.execute("DELETE FROM valve_flanged WHERE flanged_type_id = %s", [flagid])

                return JsonResponse({'status': 'success', 'message': 'flanged type deleted successfully'})
        except Exception as e:
            return JsonResponse({'status': 'failure', 'message': str(e)})

    return JsonResponse({'status': 'failure', 'message': 'Invalid request'})


#  Edit actuator type

def get_actuator_type(request, actuatorid):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM valve_actuator WHERE actuator_type_id = %s", [actuatorid])
        row = cursor.fetchone()
    
    if row:
        actuator_type_data = {
            'actuator_type_id': row[0],
            'actuator_type_name': row[1],
            'actuator_type_description': row[2]
        }
        return JsonResponse(actuator_type_data)
    else:
        return JsonResponse({'error': 'actuator type not found'}, status=404)


# View to update valve size
@csrf_exempt
def update_actuator_type(request):
    if request.method == "POST":
        actuatorid = request.POST.get('actuatorid')
        actuatorname = request.POST.get('actuatorname')
        actuatordesc = request.POST.get('actuatordesc')
        current_actuator_type_id = request.POST.get('current_actuator_type_id')

        with connection.cursor() as cursor:
            cursor.execute("""
                UPDATE valve_actuator
                SET actuator_type_name = %s, actuator_type_description = %s 
                WHERE actuator_type_id = %s
            """, [ actuatorname,actuatordesc, current_actuator_type_id])

        return JsonResponse({'status': 'success', 'message': 'actuator type updated successfully'})
    else:
        return JsonResponse({'status': 'failure', 'message': 'Invalid request'})
    

@csrf_exempt
def delete_actuatortype(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            actuatorid = data.get('id')

            # Delete from the database
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM valve_actuator WHERE actuator_type_id = %s", [actuatorid])

            return JsonResponse({'status': 'success', 'message': 'actuator type deleted successfully'})
        except Exception as e:
            return JsonResponse({'status': 'failure', 'message': str(e)})

    return JsonResponse({'status': 'failure', 'message': 'Invalid request'})


#  Edit unit type

def get_unit_type(request, unitid):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM valve_unit WHERE unit_id = %s", [unitid])
        row = cursor.fetchone()
    
    if row:
        unit_type_data = {
            'unit_id': row[0],
            'unit_name': row[1],
            'unit_description': row[2]
        }
        return JsonResponse(unit_type_data)
    else:
        return JsonResponse({'error': 'actuator type not found'}, status=404)


# View to update valve size
@csrf_exempt
def update_unit_type(request):
    if request.method == "POST":
        unitid = request.POST.get('unitid')
        unitname = request.POST.get('unitname')
        unitdes = request.POST.get('unitdes')
        current_unit_type_id = request.POST.get('current_unit_type_id')

        with connection.cursor() as cursor:
            cursor.execute("""
                UPDATE valve_unit
                SET unit_name = %s, unit_description = %s 
                WHERE unit_id = %s
            """, [ unitname,unitdes, current_unit_type_id])

        return JsonResponse({'status': 'success', 'message': 'unit updated successfully'})
    else:
        return JsonResponse({'status': 'failure', 'message': 'Invalid request'})
    

@csrf_exempt
def deleteunittype(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            unitid = data.get('unitid')

            # Delete from the database
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM valve_unit WHERE unit_id = %s", [unitid])

            return JsonResponse({'status': 'success', 'message': 'unit type deleted successfully'})
        except Exception as e:
            return JsonResponse({'status': 'failure', 'message': str(e)})

    return JsonResponse({'status': 'failure', 'message': 'Invalid request'})

@csrf_exempt

def save_product(request): 
    if request.method == "POST":
        productid = request.POST.get("productid")
        productname = request.POST.get("productname")
        productdescription = request.POST.get("productdescription")
        actuatortype = request.POST.get("actuatortype")
        valvesize = request.POST.get("valvesize")
        valveclass = request.POST.get("valveclass")
        type1 = request.POST.get("type")
        flangedtype = request.POST.get("flangedtype")
        airshellsetpressure = request.POST.get("airshellsetpressure")
        airshellholdingtime = request.POST.get("airshellholdingtime")
        airshelltestduration = request.POST.get("airshelltestduration")
        airshellallowedleak = request.POST.get("airshellallowedleak")
        hydroshellsetpressure = request.POST.get("hydroshellsetpressure")
        hydroshellholdingtime = request.POST.get("hydroshellholdingtime")
        hydroshelltestduration = request.POST.get("hydroshelltestduration")
        hydroshellallowedleak = request.POST.get("hydroshellallowedleak")
        bubbleseatsetpressure = request.POST.get("bubbleseatsetpressure")
        bubbleseatholdingtime = request.POST.get("bubbleseatholdingtime")
        bubbleseattestduration = request.POST.get("bubbleseattestduration")
        bubbleseatallowedleak = request.POST.get("bubbleseatallowedleak")
        airseatsetpressure = request.POST.get("airseatsetpressure")
        airseatholdingtime = request.POST.get("airseatholdingtime")
        airseattestduration = request.POST.get("airseattestduration")
        airseatallowedleak = request.POST.get("airseatallowedleak")
        hydroseatsetpressure = request.POST.get("hydroseatsetpressure")
        hydroseatholdingtime = request.POST.get("hydroseatholdingtime")
        hydroseattestduration = request.POST.get("hydroseattestduration")
        hydroseatallowedleak = request.POST.get("hydroseatallowedleak")
        airshellleakoption = request.POST.get("airshellleakoption")
        hydroshellleakoption = request.POST.get("hydroshellleakoption")
        bubbleseatleakoption = request.POST.get("bubbleseatleakoption")
        airseatleakoption = request.POST.get("airseatleakoption")
        hydroseatleakoption = request.POST.get("hydroseatleakoption")
        
        with connection.cursor() as cursor:
            cursor.execute("""
    INSERT INTO add_product (
        product_id, product_name, product_description, actuator_type, valve_size, valve_class, type, flanged_type,
        airshell_setpressure, airshell_holdingtime, airshell_testduration, airshell_allowedleak, hydroshell_setpressure,
        hydroshell_holdingtime, hydroshell_testduration, hydroshell_allowedleak, bubbleseat_setpressure, bubbleseat_holdingtime,
        bubbleseat_testduration, bubbleseat_allowedleak, airseat_setpressure, airseat_holdingtime, airseat_testduration,
        airseat_allowedleak, hydroseat_setpressure, hydroseat_holdingtime, hydroseat_testduration, hydroseat_allowedleak,
        airshell_leakoption, hydroshell_leakoption, bubbleseat_leakoption, airseat_leakoption, hydroseat_leakoption
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
""", [
    productid, productname, productdescription, actuatortype, valvesize, valveclass, type1, flangedtype,
    airshellsetpressure, airshellholdingtime, airshelltestduration, airshellallowedleak, hydroshellsetpressure,
    hydroshellholdingtime, hydroshelltestduration, hydroshellallowedleak, bubbleseatsetpressure, bubbleseatholdingtime,
    bubbleseattestduration, bubbleseatallowedleak, airseatsetpressure, airseatholdingtime, airseattestduration,
    airseatallowedleak, hydroseatsetpressure, hydroseatholdingtime, hydroseattestduration, hydroseatallowedleak,
    airshellleakoption, hydroshellleakoption, bubbleseatleakoption, airseatleakoption, hydroseatleakoption
])
           

        return JsonResponse({'status':'success','message':'product added successfully'})
    else:
        return JsonResponse({'status': 'failure', 'message': 'Invalid request'})

@csrf_exempt
def get_product_forupdate(request):
    
    if request.method == "POST":
        productid = request.POST.get("id")
    try:
        with connection.cursor() as cursor:
            cursor.execute("select * from add_product where product_id=%s",[productid])
            row=cursor.fetchone()
            print(row)
        if row:
            product_value = {   
            'product_id':  row[1] ,        
            'product_name':row[2], 
            'valve_size': row[3],  
            'valve_class': row[4],  
            'product_description': row[5],           
            'actuator_type': row[6],         
            'type': row[7],
            'flanged_type': row[8],
            'airshell_setpressure': row[9],  
            'airshell_holdingtime': row[10],
            'airshell_testduration': row[11],
            'airshell_allowedleak': row[12],
            'airshell_leakoption':row[13],
            'hydroshell_setpressure':row[14],
            'hydroshell_holdingtime':row[15],
            'hydroshell_testduration':row[16],
            'hydroshell_allowedleak':row[17],
            'hydroshell_leakoption':row[18],
            'bubbleseat_setpressure':row[19],
            'bubbleseat_holdingtime':row[20],
            'bubbleseat_testduration':row[21],
            'bubbleseat_allowedleak':row[22],
            'bubbleseat_leakoption':row[23],
            'airseat_setpressure':row[24],
            'airseat_holdingtime':row[25],
            'airseat_testduration':row[26],
            'airseat_allowedleak':row[27],
            'airseat_leakoption':row[28],
            'hydroseat_setpressure':row[29],
            'hydroseat_holdingtime':row[30],
            'hydroseat_testduration':row[31],
            'hydroseat_allowedleak':row[32],
            'hydroseat_leakoption':row[33] 
            }
            return JsonResponse({"status":"success","message":"datafetched successfully","fetcheddata":product_value})
        return JsonResponse({"status": "failure", "message": "data not fetched"})            
    except Exception as e:
        return JsonResponse({"status":"failure","message": str(e)})


@csrf_exempt
def addnameandage(request):
    if request.method == "POST":
        
        username = request.POST.get("name"),
        age1 = request.POST.get("age")
            
        try:
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO crud (name, age) VALUES (%s, %s)", [username, age1])
                connection.commit()
            return JsonResponse({"status": "success", "message": "Data added successfully"})
        except Exception as e:
            return JsonResponse({"status": "failure", "message": str(e)})
    
    return JsonResponse({"status": "failure", "message": "Invalid request method"})

def getrecord(request, id):
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT id, name, age FROM crud WHERE id = %s", [id])
            row = cursor.fetchone()
            if row:
                record = {
                    "id": row[0],
                    "name": row[1],
                    "age": row[2]
                }
                return JsonResponse({"status": "success", "record": record})
            return JsonResponse({"status": "failure", "message": "Record not found"})
    except Exception as e:
        return JsonResponse({"status": "failure", "message": str(e)})

@csrf_exempt
def updaterecord(request, id):
    if request.method == "POST":
        username = request.POST.get("name")
        age = request.POST.get("age")
        
        try:
            with connection.cursor() as cursor:
                cursor.execute("UPDATE crud SET name = %s, age = %s WHERE id = %s", 
                              [username, age, id])
                connection.commit()
                if cursor.rowcount > 0:
                    return JsonResponse({"status": "success", "message": "Data updated successfully"})
                return JsonResponse({"status": "failure", "message": "No record updated"})
        except Exception as e:
            return JsonResponse({"status": "failure", "message": str(e)})
    
    return JsonResponse({"status": "failure", "message": "Invalid request method"})

@csrf_exempt  # Or use csrf_protect if CSRF token is required
def deleterecord(request, id):
    if request.method == "DELETE":
        try:
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM crud WHERE id = %s", [id])
                connection.commit()
            return JsonResponse({"status": "success", "message": "Data deleted successfully"})
        except Exception as e:
            return JsonResponse({"status": "failure", "message": str(e)})

    return JsonResponse({"status": "failure", "message": "Invalid request method"})

@csrf_exempt

def get_data(request,productid):
    # if request.method == "POST":
        print(productid)
        try:
            with connection.cursor() as cursor:
                cursor.execute("select * from add_product where product_id=%s",[productid])
                row=cursor.fetchone()
                print(row)
            if row:
                product_value = {   
                'product_id':  row[1] ,        
                'product_name':row[2], 
                'valve_size': row[3],  
                'valve_class': row[4],  
                'product_description': row[5],           
                'actuator_type': row[6],         
                'type': row[7],
                'flanged_type': row[8],
                'airshell_setpressure': row[9],  
                'airshell_holdingtime': row[10],
                'airshell_testduration': row[11],
                'airshell_allowedleak': row[12],
                'airshell_leakoption':row[13],
                'hydroshell_setpressure':row[14],
                'hydroshell_holdingtime':row[15],
                'hydroshell_testduration':row[16],
                'hydroshell_allowedleak':row[17],
                'hydroshell_leakoption':row[18],
                'bubbleseat_setpressure':row[19],
                'bubbleseat_holdingtime':row[20],
                'bubbleseat_testduration':row[21],
                'bubbleseat_allowedleak':row[22],
                'bubbleseat_leakoption':row[23],
                'airseat_setpressure':row[24],
                'airseat_holdingtime':row[25],
                'airseat_testduration':row[26],
                'airseat_allowedleak':row[27],
                'airseat_leakoption':row[28],
                'hydroseat_setpressure':row[29],
                'hydroseat_holdingtime':row[30],
                'hydroseat_testduration':row[31],
                'hydroseat_allowedleak':row[32],
                'hydroseat_leakoption':row[33] 
                }
                return JsonResponse({"status":"success","message":"datafetched successfully","fetcheddata":product_value})
            return JsonResponse({"status": "failure", "message": "data not fetched"})            
        except Exception as e:
            return JsonResponse({"status":"failure","message": str(e)})
    
@csrf_exempt
def updatedata(request, productid):
    if request.method == "POST":
        try:
            productid1 = request.POST.get("productid")
            productname1 = request.POST.get("productname")
            productdescription1 = request.POST.get("productdescription")
            actuatortype1 = request.POST.get("actuatortype")
            valvesize1 = request.POST.get("valvesize")
            valveclass1 = request.POST.get("valveclass")
            type11 = request.POST.get("type")
            flangedtype1 = request.POST.get("flangedtype")
            airshellsetpressure1 = request.POST.get("airshellsetpressure")
            airshellholdingtime1 = request.POST.get("airshellholdingtime")
            airshelltestduration1 = request.POST.get("airshelltestduration")
            airshellallowedleak1 = request.POST.get("airshellallowedleak")
            hydroshellsetpressure1 = request.POST.get("hydroshellsetpressure")
            hydroshellholdingtime1 = request.POST.get("hydroshellholdingtime")
            hydroshelltestduration1 = request.POST.get("hydroshelltestduration")
            hydroshellallowedleak1 = request.POST.get("hydroshellallowedleak")
            bubbleseatsetpressure1 = request.POST.get("bubbleseatsetpressure")
            bubbleseatholdingtime1 = request.POST.get("bubbleseatholdingtime")
            bubbleseattestduration1 = request.POST.get("bubbleseattestduration")
            bubbleseatallowedleak1 = request.POST.get("bubbleseatallowedleak")
            airseatsetpressure1 = request.POST.get("airseatsetpressure")
            airseatholdingtime1 = request.POST.get("airseatholdingtime")
            airseattestduration1 = request.POST.get("airseattestduration")
            airseatallowedleak1 = request.POST.get("airseatallowedleak")
            hydroseatsetpressure1 = request.POST.get("hydroseatsetpressure")
            hydroseatholdingtime1 = request.POST.get("hydroseatholdingtime")
            hydroseattestduration1 = request.POST.get("hydroseattestduration")
            hydroseatallowedleak1 = request.POST.get("hydroseatallowedleak")
            airshellleakoption1 = request.POST.get("airshellleakoption")
            hydroshellleakoption1 = request.POST.get("hydroshellleakoption")
            bubbleseatleakoption1 = request.POST.get("bubbleseatleakoption")
            airseatleakoption1 = request.POST.get("airseatleakoption")
            hydroseatleakoption1 = request.POST.get("hydroseatleakoption")
            
            with connection.cursor() as cursor:
                cursor.execute("""
                    UPDATE add_product
                    SET
                        product_name = %s,
                        product_description = %s,
                        actuator_type = %s,
                        valve_size = %s,
                        valve_class = %s,
                        type = %s,
                        flanged_type = %s,
                        airshell_setpressure = %s,
                        airshell_holdingtime = %s,
                        airshell_testduration = %s,
                        airshell_allowedleak = %s,
                        hydroshell_setpressure = %s,
                        hydroshell_holdingtime = %s,
                        hydroshell_testduration = %s,
                        hydroshell_allowedleak = %s,
                        bubbleseat_setpressure = %s,
                        bubbleseat_holdingtime = %s,
                        bubbleseat_testduration = %s,
                        bubbleseat_allowedleak = %s,
                        airseat_setpressure = %s,
                        airseat_holdingtime = %s,
                        airseat_testduration = %s,
                        airseat_allowedleak = %s,
                        hydroseat_setpressure = %s,
                        hydroseat_holdingtime = %s,
                        hydroseat_testduration = %s,
                        hydroseat_allowedleak = %s,
                        airshell_leakoption = %s,
                        hydroshell_leakoption = %s,
                        bubbleseat_leakoption = %s,
                        airseat_leakoption = %s,
                        hydroseat_leakoption = %s
                    WHERE product_id = %s
                """, [
                    productname1, productdescription1, actuatortype1, valvesize1, valveclass1, type11, flangedtype1,
                    airshellsetpressure1, airshellholdingtime1, airshelltestduration1, airshellallowedleak1, hydroshellsetpressure1,
                    hydroshellholdingtime1, hydroshelltestduration1, hydroshellallowedleak1, bubbleseatsetpressure1, bubbleseatholdingtime1,
                    bubbleseattestduration1, bubbleseatallowedleak1, airseatsetpressure1, airseatholdingtime1, airseattestduration1,
                    airseatallowedleak1, hydroseatsetpressure1, hydroseatholdingtime1, hydroseattestduration1, hydroseatallowedleak1,
                    airshellleakoption1, hydroshellleakoption1, bubbleseatleakoption1, airseatleakoption1, hydroseatleakoption1,
                    productid
                ])
                
            return JsonResponse({"status": "success", "message": "Data updated successfully"})
        
        except Exception as e:
            logging.error(f"Error updating data: {e}")
            return JsonResponse({"status": "failure", "message": str(e)})

    return JsonResponse({"status": "failure", "message": "Invalid request method"})

@csrf_exempt
def deletegrid(request,productid):
    try:
        with connection.cursor() as cursor:
            cursor.execute('delete from add_product where product_id=%s',[productid])
            
        return JsonResponse({"status":"success","message":"Data deleted successfully"})
    
    except Exception as e:
        return JsonResponse({"status":"Failure","message":"Data not deleted"})    


@csrf_exempt
def savesetting(request):
    if request.method == "POST":
        good_result = request.POST.get('goodresult')
        bad_result = request.POST.get('badresult')
        cell_id = request.POST.get('cellid')
        hydro_leak = request.POST.get('hydroleak')
        
        print("good_result",good_result)
        
        with connection.cursor() as cursor:
            cursor.execute("insert into othersetting (Good_result,Bad_result,cell_id,Hydro_leak) values (%s,%s,%s,%s)",[good_result,bad_result,cell_id,hydro_leak])
            connection.commit()
            return JsonResponse({"status":"success","message":"Data inserted successfully"})
        return JsonResponse({"status":"Failure","message":"Data not inserted"})
    
    return JsonResponse({"status":"Failure","message":"Invalid response"})


def recent_login(request):
    with connection.cursor() as cursor:
        cursor.execute("select * from recent_login")
        val = cursor.fetchall()
        if val:
            data =[
                {"col1":row[0],"col2":row[1],"col3":row[2]}
                for row in val
            ]        
    return render(request,"recentlogin.html",{"data":data})


@login_required(login_url='/')
def dashboard(request):
    return render(request,"dashboard.html")


@login_required(login_url='/')
def tasks(request):
    return render(request,"Tasks.html")

@login_required(login_url='/')
def livestatus(request):
    return render(request,"livestatus.html")

@login_required(login_url='/')
def users(request):
    return render(request,"users.html")

@login_required(login_url='/') 
def settings(request):
    return render(request,'settings.html')

@csrf_exempt
def crud(request):
    with connection.cursor() as cursor:
        cursor.execute("select * from example")
        vali = cursor.fetchall()
        
        if vali:
            rowss = [
                {"id" : row[0],"uname" : row[1],"empid" : row[2]}
                for row in vali
            
            ]
    return render(request,"crud.html", {"row1":rowss})
       
@csrf_exempt
def savedata1(request):
    if request.method == "POST":
        username = request.POST.get("uname")
        employeeid = request.POST.get("empid")
        
        with connection.cursor() as cursor:
           cursor.execute(
        "INSERT INTO example (uname, empid) VALUES (%s, %s)",
        [username, employeeid]
    )
        return JsonResponse({"status":"success"})
    return JsonResponse({"status":"failure"})

@csrf_exempt
def edit_data(request,id):
    if request.method == "GET":
        try:
            with connection.cursor() as cursor:
                cursor.execute("select uname,empid from example where id = %s",[id])
                editvalue = cursor.fetchone()
                
                if editvalue:
                    
                    editedvalue = {
                            "uname":editvalue[0],
                            "empid":editvalue[1]
                            
                        }
                    return JsonResponse({"status":"success","value":editedvalue})
                else:
                    return JsonResponse({
                        "status": "Error",
                        "Message": "value not found"
                    })
                    
        except Exception as e:
                return JsonResponse({
                    "status": "Error",
                    "Message": str(e)
                })
    
    return JsonResponse({"status": "Error", "Message": "Invalid request method"})

@csrf_exempt
def update(request):
    if request.method == "POST":
        uname1 = request.POST.get("edituname")
        empid1 = request.POST.get("editempid")
        id = request.POST.get("id")
        
        try:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "UPDATE example SET uname = %s, empid = %s WHERE id = %s",
                        [uname1, empid1, id]
                    )
                return JsonResponse({"status": "success"})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)})

    return JsonResponse({"status": "failure", "message": "Invalid method"})

@csrf_exempt
def resourcemgnt(request):
    with connection.cursor() as cursor:
        cursor.execute("select * from valve_size")
        newvalue = cursor.fetchall()
        if newvalue:
            data = [{
                "sizeid":row[0],
                "sizename":row[1],
                "sizedesc":row[2]
                
            }
                for row in newvalue
            ]
            
        with connection.cursor() as cursor:
            cursor.execute("select * from valve_type")
            newvalue1 = cursor.fetchall()
            if(newvalue1):
                data2 = [{
                    "typeid":row[0],
                    "typename":row[1],
                    "typedesc":row[2]
                }   
                    for row in newvalue1
                ]      
                
        with connection.cursor() as cursor:
            cursor.execute("select * from valve_class")
            valveclass = cursor.fetchall()
            if(valveclass):
                data3 = [{
                    "classid":row[0],
                    "classname":row[1],
                    "classdesc":row[2]
                }
                         for row in valveclass
                ]
                
        with connection.cursor() as cursor:
            cursor.execute("select * from valve_flanged")
            valveflanged = cursor.fetchall()
            if valveflanged:
                data4 = [{
                    "flangedid":row[0],
                    "flangedname":row[1],
                    "flangeddesc":row[2]
                }
                    for row in valveflanged         
                ]
                
        with connection.cursor() as cursor:
            cursor.execute("select * from valve_actuator")
            valveactuator = cursor.fetchall()
            if valveactuator:
                data5 = [{
                    "actuatorid":row[0],
                    "actuatorname":row[1],
                    "actuatordesc":row[2]
                }
                    for row in valveactuator         
                ]
                
        with connection.cursor() as cursor:
            cursor.execute("select * from valve_unit")
            valveunit = cursor.fetchall()
            if valveunit:
                data6 = [{
                    "unitid":row[0],
                    "unitname":row[1],
                    "unitdesc":row[2]
                }
                    for row in valveunit         
                ]
                
        with connection.cursor() as cursor:
            cursor.execute("select * from add_product")
            product = cursor.fetchall()
        
            data7 = [
                    {"row1":row[1], "row2":row[2], "row3":row[3],"row4":row[4]}
                    for row in product
                ]
        
    return render(request,"resourcemgnt.html",{"data1":data,"data2":data2,"data3":data3,"data4":data4,"data5":data5,"data6":data6,"data7":data7})

@csrf_exempt
def savevalvedata(request):
    if request.method == "POST":
        
        size_id = request.POST.get("sizeid")
        size_name = request.POST.get("sizename")
        size_desc = request.POST.get("sizedesc")
        
        
        with connection.cursor() as cursor:
            cursor.execute(
        "INSERT INTO valve_size (valve_size_id, valve_size_name, valve_size_description) VALUES (%s, %s, %s)",
        [size_id, size_name, size_desc]
    )

            
            return JsonResponse({"status":"success"})
        
    return JsonResponse({"status":"failure"})

@csrf_exempt
def deletedata(request):
    if request.method=="POST":
        deleteid = request.POST.get('id')
        
        with connection.cursor() as cursor:
            cursor.execute("delete from valve_size where valve_size_id=%s",[deleteid])
            
            return JsonResponse({"status":"success"})
    return JsonResponse({"status":"failure"})

@csrf_exempt
def get_data_for_edit(request):
    if request.method == "POST":
        size_id = request.POST.get('size')
        
    with connection.cursor() as cursor:
        cursor.execute("select valve_size_id,valve_size_name,valve_size_description from valve_size where valve_size_id = %s",[size_id])
        edit = cursor.fetchone()
        if edit:
            data = {
                    "size_id": edit[0],
                    "size_name": edit[1],
                    "size_desc": edit[2]
                }
                
            
        return JsonResponse({"status":"success","data1":data})
            
    return JsonResponse({"status":"failure"})

@csrf_exempt
def save_updateddata(request):
    if request.method == "POST":
        updateone1 = request.POST.get("updateone1")
        updateone2 = request.POST.get("updateone2")
        updateone3 = request.POST.get("updateone3")
        updateid = request.POST.get("id")
        
    with connection.cursor() as cursor:
        cursor.execute(
            "UPDATE valve_size SET valve_size_id = %s, valve_size_name = %s, valve_size_description = %s WHERE valve_size_id = %s",
            [updateone1, updateone2, updateone3, updateid]
            )
        return JsonResponse({"status":"success"})
    return JsonResponse({"status":"failure"})
        
@csrf_exempt
def save_classtype(request):
    if request.method == "POST":
        typeid = request.POST.get("typeid")
        typename = request.POST.get("typename")
        typedesc = request.POST.get("typedesc")

       
        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO valve_type (valve_type_id, valve_type_name, valve_type_description)
                VALUES (%s, %s, %s)
            """, [typeid, typename, typedesc])
            return JsonResponse({"status": "success"})
        

    return JsonResponse({"status": "failure"})

@csrf_exempt
def save_valveclass(request):
    if request.method == "POST":
        classid = request.POST.get("classid")
        classname = request.POST.get("classname")
        classdesc = request.POST.get("classdesc")

        
        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO valve_class (valve_class_id, valve_class_name, valve_class_description)
                VALUES (%s, %s, %s)
            """, [classid, classname, classdesc])
        return JsonResponse({"status": "success"})
        
              
    return JsonResponse({"status": "failure"})

@csrf_exempt
def get_update_classtype(request):
    if request.method == "POST":
        id = request.POST.get('id')
        print(id)
        
        with connection.cursor() as cursor:
            cursor.execute("SELECT valve_type_id, valve_type_name, valve_type_description FROM valve_type WHERE valve_type_id = %s", [id])
            update = cursor.fetchone()

            if update:
                data3 = {
                    "typeidupdate": update[0],
                    "typenameupdate": update[1],
                    "typedesc": update[2]
                }
                return JsonResponse({"status": "success", "data3": data3})
            else:
                return JsonResponse({"status": "not_found", "message": "Valve type not found."})

    return JsonResponse({"status": "failure", "message": "Invalid request method."})


@csrf_exempt
def save_editedclasstype(request):
    if request.method == "POST":
        updatetypeid = request.POST.get('updatetypeid')
        updatetypename = request.POST.get('updatetypename')
        updatetypedesc = request.POST.get('updatetypedesc')
        currentid = request.POST.get('currentid')
        
        with connection.cursor() as cursor:
            cursor.execute("update valve_type set valve_type_id=%s,valve_type_name=%s,valve_type_description=%s where valve_type_id=%s ",[updatetypeid,updatetypename,updatetypedesc,currentid])
        return JsonResponse({"status":"success"})            
    return JsonResponse({"status":"failure"})

@csrf_exempt
def delete_valvetype(request):
    if request.method == "POST":
        id = request.POST.get("id")
        
        with connection.cursor() as cursor:
            cursor.execute("delete from valve_type where valve_type_id=%s",[id])
        return JsonResponse({"status":"success"})            
    return JsonResponse({"status":"failure"})


# @csrf_exempt
# def save_valveclass(request):
#     if request.method == "POST":
#         classid = request.POST.get("classid")
#         classname = request.POST.get("classname")
#         classdes = request.POST.get("classdes")
        
#         with connection.cursor() as cursor:
#             cursor.execute("insert into valve_class (valve_class_id,valve_class_name,valve_class_description) values(%s,%s,%s)",[classid,classname,classdes])
#         return JsonResponse({"status":"success"})      
#     return JsonResponse({"status":"failure"})      

@csrf_exempt
def fetch_classdata(request):
    if request.method == "POST":
        classid = request.POST.get("id")
        
        with connection.cursor() as cursor:
            cursor.execute("select valve_class_id,valve_class_name,valve_class_description from valve_class where valve_class_id=%s",[classid])
            
            classvalue= cursor.fetchone()
            
            data = {
                "classid":classvalue[0],
                "classname":classvalue[1],
                "classdes":classvalue[2]   
            }
            return JsonResponse({"status":"success","data4":data})
    return JsonResponse({"status":"failure"})



@csrf_exempt
def delete_valveclass(request):
    if request.method == "POST":
        id = request.POST.get("id")
        
        with connection.cursor() as cursor:
            cursor.execute("delete from valve_class where valve_class_id=%s",[id])
        return JsonResponse({"status":"success"})            
    return JsonResponse({"status":"failure"})

@csrf_exempt
def save_updatedclass(request):
   if request.method == "POST":
       updateclassid = request.POST.get('updateclassid')
       updateclassname = request.POST.get('updateclassname')
       updateclassdes = request.POST.get('updateclassdes')
       classid = request.POST.get('classid')
       
       with connection.cursor() as cursor:
           cursor.execute("update valve_class set valve_class_id=%s,valve_class_name=%s,valve_class_description=%s where valve_class_id=%s",[updateclassid,updateclassname,updateclassdes,classid])  
           return JsonResponse({"status":"success"})
       return JsonResponse({"status":"failure"})

@csrf_exempt
def save_flangeddata(request):
    if request.method == "POST":
        flagid = request.POST.get("flagid")
        flagname = request.POST.get("flagname")
        flagdesc = request.POST.get("flagdesc")
        
        with connection.cursor() as cursor:
            cursor.execute("insert into valve_flanged (flanged_type_id,flanged_type_name,flanged_type_description) values (%s,%s,%s)",[flagid,flagname,flagdesc])
        return JsonResponse({"status":"success"})
    return JsonResponse({"status":"failure"})

@csrf_exempt
def fetch_flangdata(request):
    if request.method == "POST":
        flangid = request.POST.get("id")
        
        with connection.cursor() as cursor:
            cursor.execute("SELECT flanged_type_id, flanged_type_name, flanged_type_description FROM valve_flanged WHERE flanged_type_id = %s", [flangid])
            flangvalue = cursor.fetchone()

            if flangvalue:
                data = {
                    "flangid": flangvalue[0],
                    "flangname": flangvalue[1],
                    "flangdes": flangvalue[2]
                }
                return JsonResponse({"status": "success", "data5": data})
            else:
                return JsonResponse({"status": "failure", "message": "No data found for the given flanged_type_id"})
    else:
        return JsonResponse({"status": "failure", "message": "Invalid request"})


@csrf_exempt
def save_updatedflang(request):
    if request.method == "POST":
        updateflagid = request.POST.get('updateflagid')
        updateflagname = request.POST.get('updateflagname')
        updateflagdesc = request.POST.get('updateflagdesc')
        currentflangedid = request.POST.get('currentflangedid')
        
        with connection.cursor() as cursor:
            cursor.execute("update valve_flanged set flanged_type_id=%s,flanged_type_name=%s,flanged_type_description=%s where flanged_type_id=%s ",[updateflagid,updateflagname,updateflagdesc,currentflangedid])
        return JsonResponse({"status":"success"})            
    return JsonResponse({"status":"failure"})

@csrf_exempt
def save_actuator(request):
    if request.method == "POST":
        actuatorid = request.POST.get("actuatorid")
        actuatorname = request.POST.get("actuatorname")
        actuatordesc = request.POST.get("actuatordesc")
        
        with connection.cursor() as cursor:
            cursor.execute("insert into valve_actuator (actuator_type_id,actuator_type_name,actuator_type_description) values(%s,%s,%s)",[actuatorid,actuatorname,actuatordesc])
        return JsonResponse({"status":"success"})      
    return JsonResponse({"status":"failure"}) 

@csrf_exempt
def getvalue_forupdate(request):
    if request.method == "POST":
        actuatorid = request.POST.get("id")
        
        with connection.cursor() as cursor:
            cursor.execute("SELECT actuator_type_id, actuator_type_name, actuator_type_description FROM valve_actuator WHERE actuator_type_id = %s", [actuatorid])
            actuatorvalue = cursor.fetchone()

            if actuatorvalue:
                data = {
                    "flangid": actuatorvalue[0],
                    "flangname": actuatorvalue[1],
                    "flangdes": actuatorvalue[2]
                }
                return JsonResponse({"status": "success", "data6": data})
            else:
                return JsonResponse({"status": "failure", "message": "No data found for the given flanged_type_id"})
    else:
        return JsonResponse({"status": "failure", "message": "Invalid request"})
    
@csrf_exempt
def save_updated_actuator(request):
    if request.method == "POST":
        updateactuatorid = request.POST.get('updateactuatorid')
        updateactuatorname = request.POST.get('updateactuatorname')
        updateactuatordesc = request.POST.get('updateactuatordesc')
        currentactuatorid = request.POST.get('currentactuatorid')
        
        with connection.cursor() as cursor:
            cursor.execute("update valve_actuator set actuator_type_id=%s,actuator_type_name=%s,actuator_type_description=%s where actuator_type_id=%s ",[updateactuatorid,updateactuatorname,updateactuatordesc,currentactuatorid])
        return JsonResponse({"status":"success"})            
    return JsonResponse({"status":"failure"})

@csrf_exempt
def delete_actuator(request):
    if request.method == "POST":
        id = request.POST.get("id")
        
        with connection.cursor() as cursor:
            cursor.execute("delete from valve_actuator where actuator_type_id=%s",[id])
        return JsonResponse({"status":"success"})            
    return JsonResponse({"status":"failure"})

@csrf_exempt
def save_unit(request):
    if request.method == "POST":
        unitid = request.POST.get("unitid")
        unitname = request.POST.get("unitname")
        unitdes = request.POST.get("unitdes")
        
        with connection.cursor() as cursor:
            cursor.execute("insert into valve_unit (unit_id,unit_name,unit_description) values(%s,%s,%s)",[unitid,unitname,unitdes])
        return JsonResponse({"status":"success"})      
    return JsonResponse({"status":"failure"})

@csrf_exempt
def getunit_forupdate(request):
    if request.method == "POST":
        unitid = request.POST.get("id")
        
        with connection.cursor() as cursor:
            cursor.execute("SELECT unit_id, unit_name, unit_description FROM valve_unit WHERE unit_id = %s", [unitid])
            unitvalue = cursor.fetchone()

            if unitvalue:
                data = {
                    "unitid": unitvalue[0],
                    "unitname": unitvalue[1],
                    "unitdes": unitvalue[2]
                }
                return JsonResponse({"status": "success", "data7": data})
            else:
                return JsonResponse({"status": "failure", "message": "No data found for the given flanged_type_id"})
    else:
        return JsonResponse({"status": "failure", "message": "Invalid request"})
    
@csrf_exempt
def save_updated_unit(request):
    if request.method == "POST":
        updateunitid = request.POST.get('updateunitid')
        updateunitname = request.POST.get('updateunitname')
        updateunitdes = request.POST.get('updateunitdes')
        currentunitid = request.POST.get('currentunitid')
        
        with connection.cursor() as cursor:
            cursor.execute("update valve_unit set unit_id=%s,unit_name=%s,unit_description=%s where unit_id=%s ",[updateunitid,updateunitname,updateunitdes,currentunitid])
        return JsonResponse({"status":"success"})            
    return JsonResponse({"status":"failure"})


@csrf_exempt
def delete_unit(request):
    if request.method == "POST":
        id = request.POST.get("id")
        
        with connection.cursor() as cursor:
            cursor.execute("delete from valve_unit where unit_id=%s",[id])
        return JsonResponse({"status":"success"})            
    return JsonResponse({"status":"failure"})

@csrf_exempt
def save_updatedproduct(request):
    if request.method == "POST":
        try:
            id = request.POST.get('id')
            productid = request.POST.get('currentproductid')
            productname1 = request.POST.get("productname")
            productdescription1 = request.POST.get("productdescription")
            actuatortype1 = request.POST.get("actuatortype")
            valvesize1 = request.POST.get("valvesize")
            valveclass1 = request.POST.get("valveclass")
            type11 = request.POST.get("type")
            flangedtype1 = request.POST.get("flangedtype")
            airshellsetpressure1 = request.POST.get("airshellsetpressure")
            airshellholdingtime1 = request.POST.get("airshellholdingtime")
            airshelltestduration1 = request.POST.get("airshelltestduration")
            airshellallowedleak1 = request.POST.get("airshellallowedleak")
            hydroshellsetpressure1 = request.POST.get("hydroshellsetpressure")
            hydroshellholdingtime1 = request.POST.get("hydroshellholdingtime")
            hydroshelltestduration1 = request.POST.get("hydroshelltestduration")
            hydroshellallowedleak1 = request.POST.get("hydroshellallowedleak")
            bubbleseatsetpressure1 = request.POST.get("bubbleseatsetpressure")
            bubbleseatholdingtime1 = request.POST.get("bubbleseatholdingtime")
            bubbleseattestduration1 = request.POST.get("bubbleseattestduration")
            bubbleseatallowedleak1 = request.POST.get("bubbleseatallowedleak")
            airseatsetpressure1 = request.POST.get("airseatsetpressure")
            airseatholdingtime1 = request.POST.get("airseatholdingtime")
            airseattestduration1 = request.POST.get("airseattestduration")
            airseatallowedleak1 = request.POST.get("airseatallowedleak")
            hydroseatsetpressure1 = request.POST.get("hydroseatsetpressure")
            hydroseatholdingtime1 = request.POST.get("hydroseatholdingtime")
            hydroseattestduration1 = request.POST.get("hydroseattestduration")
            hydroseatallowedleak1 = request.POST.get("hydroseatallowedleak")
            airshellleakoption1 = request.POST.get("airshellleakoption")
            hydroshellleakoption1 = request.POST.get("hydroshellleakoption")
            bubbleseatleakoption1 = request.POST.get("bubbleseatleakoption")
            airseatleakoption1 = request.POST.get("airseatleakoption")
            hydroseatleakoption1 = request.POST.get("hydroseatleakoption")
            
            with connection.cursor() as cursor:
                cursor.execute("""
                UPDATE add_product
                SET
                    product_name = %s,
                    product_description = %s,
                    actuator_type = %s,
                    valve_size = %s,
                    valve_class = %s,
                    type = %s,
                    flanged_type = %s,
                    airshell_setpressure = %s,
                    airshell_holdingtime = %s,
                    airshell_testduration = %s,
                    airshell_allowedleak = %s,
                    hydroshell_setpressure = %s,
                    hydroshell_holdingtime = %s,
                    hydroshell_testduration = %s,
                    hydroshell_allowedleak = %s,
                    bubbleseat_setpressure = %s,
                    bubbleseat_holdingtime = %s,
                    bubbleseat_testduration = %s,
                    bubbleseat_allowedleak = %s,
                    airseat_setpressure = %s,
                    airseat_holdingtime = %s,
                    airseat_testduration = %s,
                    airseat_allowedleak = %s,
                    hydroseat_setpressure = %s,
                    hydroseat_holdingtime = %s,
                    hydroseat_testduration = %s,
                    hydroseat_allowedleak = %s,
                    airshell_leakoption = %s,
                    hydroshell_leakoption = %s,
                    bubbleseat_leakoption = %s,
                    airseat_leakoption = %s,
                    hydroseat_leakoption = %s
                WHERE product_id = %s
            """, [
                productname1, productdescription1, actuatortype1, valvesize1, valveclass1,
                type11, flangedtype1, airshellsetpressure1, airshellholdingtime1, airshelltestduration1, airshellallowedleak1,
                hydroshellsetpressure1, hydroshellholdingtime1, hydroshelltestduration1, hydroshellallowedleak1,
                bubbleseatsetpressure1, bubbleseatholdingtime1, bubbleseattestduration1, bubbleseatallowedleak1,
                airseatsetpressure1, airseatholdingtime1, airseattestduration1, airseatallowedleak1,
                hydroseatsetpressure1, hydroseatholdingtime1, hydroseattestduration1, hydroseatallowedleak1,
                airshellleakoption1, hydroshellleakoption1, bubbleseatleakoption1, airseatleakoption1, hydroseatleakoption1,
                id
            ])

                
            return JsonResponse({"status": "success", "message": "Data updated successfully"})
        
        except Exception as e:
            logging.error(f"Error updating data: {e}")
            return JsonResponse({"status": "failure", "message": str(e)})

    return JsonResponse({"status": "failure", "message": "Invalid request method"})

@csrf_exempt
def delete_product(request):
    if request.method == "POST":
        id = request.POST.get("id")
        with connection.cursor() as cursor:
            cursor.execute('delete from add_product where product_id=%s',[id])
            
        return JsonResponse({"status":"success","message":"Data deleted successfully"})
    
    
    return JsonResponse({"status":"Failure","message":"Data not deleted"})

@csrf_exempt
def logout_view(request):
    logout(request) 
    return redirect('/') 