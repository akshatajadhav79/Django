from django.shortcuts import render,HttpResponseRedirect
from django.contrib import messages
from staff.models import MenuMaster ,staffMaster,staffTypesMaster
from django.http import JsonResponse
from django.contrib.auth import authenticate ,logout,login
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/accounts/login/')   
def Newstaff(request):
    if request.method=="POST":
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        address=request.POST.get('address')
        contact=request.POST.get('contact')
        hiredDate=request.POST.get('hiredDate')
        position=request.POST.get('position')
        pic=request.FILES.get('pic')
        DOB=request.POST.get('DOB')
        if staffMaster.objects.filter(email=email).exists():
            messages.error(request,"Email is Already exsist..!")
            return HttpResponseRedirect(request.path_info)
        else:       
            staffMaster.objects.create(first_name=first_name, last_name=last_name
                                        ,contact=contact,address=address,email=email,
                                        hiredDate=hiredDate,position_id=position,
                                        pic=pic,DOB=DOB)
            messages.success(request,"Staff is created successfully..!")
        
    
    all_urls= MenuMaster.objects.all()
    st= staffTypesMaster.objects.all()
    sm = staffMaster.objects.all()
    context = {"menu": all_urls,"st":st,"sm":sm}
    return render(request,"staff/staffhome.html",context)
    
@login_required(login_url='/accounts/login/')   
def staffType(request, id=None):
    if request.method=="POST":
        Tname=request.POST.get('Tname')
        id = request.POST.get('id')
        
        
        if 'submit' in request.POST and request.POST['submit'] == 'save':
            print("save")
            if staffTypesMaster.objects.filter(Tname=Tname).exists():
                messages.error(request,"Type is Already exsist..!")
                return HttpResponseRedirect(request.path_info)
            else:       
                staffTypesMaster.objects.create(Tname=Tname )
                messages.success(request,"Type is created successfully")
                
        elif 'submit' in request.POST and request.POST['submit'] == 'cancel':
            print('cancel')
            return HttpResponseRedirect(request.path_info)
        
        elif 'submit' in request.POST and request.POST['submit'] == 'delete':
            if id:
                st = staffTypesMaster.objects.get(STid=id)
                st.delete()
                messages.success(request, "Type is deleted successfully")
                
        elif 'submit' in request.POST and request.POST['submit'] == 'Edit':
            if id is not None:
        
                # Retrieve the staff type to update
                staff_type = staffTypesMaster.objects.get(STid=id)
                print("stid=", staff_type)
                
                # Get the current name of the staff type
                current_name = staff_type.Tname
                print(current_name)
                
                all_urls= MenuMaster.objects.all()
                type = staffTypesMaster.objects.all()
                context = {"type":type,"Tname": current_name,"id":id ,'menu':all_urls}
                return render(request, "staff/staffType.html", context)
            
      
        elif 'submit' in request.POST and request.POST['submit'] == 'update':
                print("update")
                if id is not None:
                    print(id)
                    staff_type = staffTypesMaster.objects.get(STid=id)
                    print("stid=", staff_type)
                    if request.method == "POST":
                        new_name = request.POST.get('Tname')
                        print(new_name)
                        
                        if new_name is not None:
                            # Update the name of the staff type
                            staff_type.Tname = new_name
                            staff_type.save()
                            messages.success(request, "Type is updated successfully")
                            return HttpResponseRedirect("/staff/staffType")
                        else:
                            messages.error(request, "New Tname is required for the update.")
                            return HttpResponseRedirect(request.path_info)
                               
                type = staffTypesMaster.objects.all()
                context = {"type":type,"Tname": current_name,"id":id ,}
                return render(request, "staff/staffType.html",context)
        
    type = staffTypesMaster.objects.all()
    all_urls= MenuMaster.objects.all()
    context = {"type":type,"menu": all_urls}
    return render(request,"staff/staffType.html", context)

# @login_required(login_url='/accounts/login/')   
# def del_staff(request,id):
#     st=staffTypesMaster.objects.get(STid=id)
#     st.delete()
#     messages.error(request,"Deleted..!")
#     return HttpResponseRedirect("/staff/staffType")

@login_required(login_url='/accounts/login/')   
def del_sm(request,id):
    st=staffMaster.objects.get(sid=id)
    st.delete()
    messages.error(request,"Deleted..!")
    return HttpResponseRedirect("/staff/staffhome")

# @login_required(login_url='/accounts/login/')   
# def upTy(request,id):
    ut = staffTypesMaster.objects.get(STid=id)
    Tname=ut.Tname
    if request.method=="POST":
        Tname=request.POST.get('Tname')
        if  staffTypesMaster.objects.filter(Tname=Tname).exists():
            messages.error(request,"Type is Already exsist..!")
            return HttpResponseRedirect(request.path_info)
        else:       
            ut.Tname=Tname 
            ut.save()
            messages.success(request,"Type is Updated successfully")
            return HttpResponseRedirect("/staff/staffType")
   
    all_urls= MenuMaster.objects.all()
    type = staffTypesMaster.objects.all()
    context = {"Tname":Tname,"menu": all_urls ,"type":type}
    return render(request,"staff/staffType.html",context)