from django.conf import settings
from django.shortcuts import render,redirect,HttpResponseRedirect,HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from accounts.models import ServiceMaster, contactMaster,AdvatureMaster,BookingMaster ,User
from django.db.models import Q
from django.core.paginator import Paginator
from django.core.mail import EmailMessage,send_mail
from staff.models import MenuMaster
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,logout,login
from django.contrib.auth.decorators import login_required


# Create your views here.

def reset_password(request):
    if request.method == "POST":
        email=request.POST.get('email')
        
        if 'submit' in request.POST and request.POST['submit'] == 'send':
            print("send",email)
            if email is not None:
                eng=User.objects.filter(email = email)
                if eng.exists():
                    agent = User.objects.get(email=email)
                    
                    subject = "Welcome to Django Wdding PLanner Pro...!!"
                    message = "Hello"+ agent.first_name + "!! \n"+ "Thank you for visiting our website \n Thanking You..! Please open Mail to verify your email address..!"
                    from_email = settings.EMAIL_HOST_USER
                    to_list = [agent.email]
                    send_mail(subject , message , from_email ,to_list ,fail_silently=True)
                
                    context = {"agent":agent}
                    return render(request,"accounts/reset_password.html",context)
                else:
                    messages.success(request, "Email does't Exsist")
                    return HttpResponseRedirect("/accounts/reset_password")
        
        elif 'submit' in request.POST and request.POST['submit'] == 'Reset':
                print("reset")
                if request.method == "POST":
                    new_email = request.POST.get('email')
                    new_pass =request.POST.get('password')
                    cpass = request.POST.get('cpassword')
                    print(new_pass,email)
                    try:
                        if new_email is not None:
                            if User.objects.filter(email=new_email).exists():
                                user= User.objects.get(email=new_email)
                                if new_pass == cpass:
                                    user.set_password(new_pass)
                                    hashed_password = make_password(new_pass)
                                    user.password = hashed_password
                                    user.save()
                                else:
                                    messages.error(request,"Password does't match")
                                    return HttpResponseRedirect("/accounts/reset_password")
                            else:
                                messages.error(request,"Email is does't exists")
                                return HttpResponseRedirect("/accounts/reset_password")
                        
                            messages.success(request, "Password is updated successfully")
                            return HttpResponseRedirect("/accounts/login/")
                    
                    except User.DoesNotExist:
                        print(f"User with username {email} does not exist.")
                        messages.success(request,"Password reset successfully")
                else:
                    messages.error(request, "Email is required for the Change Password.")
                    return HttpResponseRedirect(request.path_info)
            
    return render(request,"accounts/reset_password.html")

def login_page(request): 
    if request.method == "POST":
        username=request.POST.get('username')
        password= request.POST.get('password')
        
        if not User.objects.filter(username=username).exists():
            messages.error(request,"Invalid Username ")
            return redirect('/accounts/login/') 
        
        user=authenticate(username=username,password=password)
        
        if user is None:
            messages.error(request,"Invalid Password ")
            return redirect('/accounts/login/')
        
        else:
            #session method use to store user
            login(request,user) 
            return redirect('/base/')
    all_urls= MenuMaster.objects.all()
    context={'all':all ,"menu": all_urls}
    return render(request,'accounts/login.html',context)


def logout_user(request):
    logout(request)
    messages.success(request,"Logged out Successfully")
    return HttpResponseRedirect('/accounts/login/')

def register(request):
    if request.method =="POST":
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        username=request.POST.get('username')
       
        user=User.objects.filter(email = email)
        if user.exists():
            messages.error(request,'Email is Already taken')
            return HttpResponseRedirect(request.path_info)
        else:   
            user=User.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email, username=username
            )
        user.set_password(password)
        user.save()
        messages.success(request,"your account created successfully.")
        
        # welcome Email
        subject = "Welcome to Django Precious Nature Hotel...!!"
        message = "Hello"+ user.first_name + "!! \n"+ "Thank you for visiting our website \n Thanking You..!"
        from_email = settings.EMAIL_HOST_USER
        to_list = [user.email]
        send_mail(subject , message , from_email ,to_list ,fail_silently=True)
        
        return redirect("/accounts/login/")
            
     
    return render(request,'accounts/register.html')
    
#---------------------------------------------------------------------------------------------------------   
@login_required(login_url='/accounts/login/')
def User_view(request):
    users=User.objects.all()
    all_urls= MenuMaster.objects.all()
    #search BAR
    if request.GET.get('search'):
        search =request.GET.get('search')
        users=users.filter(
            Q(id__icontains=search)|
            Q(email__icontains=search)|
            Q(email__icontains=search)|
            Q(first_name__icontains=search)|
            Q(last_name__icontains=search)|
            Q(date_joined__icontains=search)  
        )
        
        #paginator add
        # paginator=Paginator(users,10)
        # page_number=request.GET.get("page",1)
        # page_obj=paginator.get_page(page_number)
        
        # print(page_obj.object_list)
             
    context={'users':users , "menu": all_urls}
    return render( request,"accounts/Userview.html",context)

@login_required(login_url='/accounts/login/')
def update_muser(request,id):
    print(id)
    idr= User.objects.get(id=id)
    if request.method=="POST":
        data= request.POST
        
        first_name=data.get('first_name')
        last_name=data.get('last_name')
        email=data.get('email')
        is_active=data.get('is_active')
        print(is_active)
        is_staff=data.get('is_staff')
        print(is_staff)
        is_superuser=data.get('is_superuser')
        
        idr.first_name=first_name
        idr.last_name=last_name
        idr.email=email
       
       
        if is_active == 'on':
            idr.is_active= True
        else:
            idr.is_active=False    
        if is_staff == 'on':
            idr.is_staff= True
        else:
            idr.is_staff=False   
        if is_superuser == 'on':
            idr.is_superuser=True
            idr.is_active=True
            idr.is_staff=True
        else:
            idr.is_superuser=False
        
        
        idr.save()
        return redirect('/base')
    all_urls=MenuMaster.objects.all()
    context={'idr':idr ,"menu": all_urls} 
    return render(request,'accounts/update_user.html',context)

@login_required(login_url='/accounts/login/')   
def delete_user(request,id):
    user1=User.objects.get(id=id)
    user1.delete()
    messages.error(request,"Account Deleted Successfully")
    return redirect('/accounts/Userview/')    
  


#contactMaster-------------------------------------------------------------------------------------------------
 
def contact_master(request):
    if request.method=="POST":
        cname=request.POST.get('cname')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
       
        #search BAR users=User.objects.all()
    
        coustmer=contactMaster.objects.filter(cname=cname)
        if coustmer.exists():
            messages.warning(request,"You Already send message...! ")
            return HttpResponseRedirect(request.path_info)
        
        feedback=contactMaster.objects.create(cname=cname , email=email , subject=subject , message=message)
        feedback.save() 
        messages.success(request,"You succesfully send message..! Thank you")
        return redirect('/accounts/contact')
    
    all_urls= MenuMaster.objects.all()
    context={'all':all ,"menu": all_urls}
    return render(request,'products/contact_master.html',context)

#TO view contact messages
@login_required(login_url='/accounts/login/')   
def contactview(request):
    all_urls= MenuMaster.objects.all()
    all=contactMaster.objects.all()
     #search BAR
    if request.GET.get('search'):
        search =request.GET.get('search')
        all=all.filter(
            Q(id__icontains=search)|
            Q(cname__icontains=search)|
            Q(email__icontains=search)|
            Q(subject__icontains=search)  
        )
    context={'all':all ,"menu": all_urls}
    return render(request,'tables/contactview.html',context)

@login_required(login_url='/accounts/login/')   
def delete_cust(request,id):
    cust=contactMaster.objects.get(id=id)
    cust.delete()
    messages.error(request,"Deleted")
    return redirect("/accounts/contactview/")

#----------------------------------------------------------------------------------------------------------   


#AdvantureMaster
@login_required(login_url='/accounts/login/')   
def advature_master(request):
    all_urls= MenuMaster.objects.all()
    user=User.objects.all()
    all=AdvatureMaster.objects.all()
    
     
    if request.method=="POST":
        adv_name=request.POST.get("adv_name")
        adv_details=request.POST.get("adv_details")
        adv_charges=request.POST.get("adv_charges")
        host=request.POST.get("host")
        search = request.POST.get('search')
        
        print(search,adv_charges,adv_details,adv_name)
        if 'submit' in request.POST and request.POST['submit'] == 'save':
            
            adv=AdvatureMaster.objects.filter(adv_name=adv_name)
            if adv.exists():
                messages.error(request,"Advature name is exists.")
                return HttpResponseRedirect(request.path_info)
            
            adv=AdvatureMaster.objects.create(
                adv_name=adv_name,
                adv_details=adv_details,
                adv_charges=adv_charges,user_id=host
            )
            messages.success(request,"Advanture create successfully")
        
        elif 'submit' in request.POST and request.POST['submit'] == 'search':
            if search:
                all = all.filter(
                    Q(uid__icontains=search)|
                    Q(adv_name__icontains=search)|
                    Q(adv_details__icontains=search)|
                    Q(adv_charges__icontains=search) |
                    Q(user__first_name__icontains=search) |
                    Q(user__last_name__icontains=search) 
                )
                
        if 'submit' in request.POST and request.POST['submit'] == 'delete':
            if request.method=="POST":
                ad_id=request.POST.get('id')
                ad=AdvatureMaster.objects.get(uid=ad_id)
                ad.delete()
                messages.error(request,"service is deleted")
                return HttpResponseRedirect(request.path_info)
        
    context={'user':user, 'all':all, "menu": all_urls}
    return render(request,'tables/AdvatureMaster.html',context)
#------------------------------------------------------------------------------------------------------------

#ServicesMaster
@login_required(login_url='/accounts/login/')   
def  service_master(request):
    all_urls= MenuMaster.objects.all()
    user=User.objects.all()
    all=ServiceMaster.objects.all()
    
    if request.GET.get('search'):
        search =request.GET.get('search')
        all=all.filter(
            Q(uid__icontains=search)|
            Q(service_name__icontains=search)|
            Q(service_details__icontains=search)|
            Q(service_cost__icontains=search) |
            Q(user__first_name__icontains=search)   
        )
    context={'user':user,'all':all, "menu": all_urls}
    
    if 'submit' in request.POST and request.POST['submit'] == 'save':
        if request.method=="POST":
            service_name=request.POST.get('service_name')
            service_details=request.POST.get('service_details')
            service_cost=request.POST.get('service_cost')
            service_img=request.FILES.get('service_img')
            user=request.POST.get('host')
            print(user)
            
            ser = ServiceMaster.objects.filter(service_name=service_name)
            if ser.exists():
                messages.error(request,"service is Already exsist..!")
                return HttpResponseRedirect(request.path_info)
            elif int(service_cost) > 99999999:
                messages.error(request,"service cost is TO large..please Enter right cost")
                return HttpResponseRedirect(request.path_info)
            else:
                ser=ServiceMaster.objects.create(
                    service_name=service_name, service_cost=service_cost ,service_img=service_img , service_details=service_details ,
                    user_id=user
                )
                messages.success(request,"service create successfully")
            
    if 'submit' in request.POST and request.POST['submit'] == 'delete':
        if request.method=="POST":
            service_id=request.POST.get('id')
            service=ServiceMaster.objects.get(uid=service_id)
            service.delete()
            messages.error(request,"service is deleted")
            return HttpResponseRedirect(request.path_info)
        
        
    return render(request,'tables/ServicesMaster.html',context)


#---------------------------------------------------------------------------------------------------------------

#BookingMaster
 
def  booking_master(request):
    service= ServiceMaster.objects.all()
    advature=AdvatureMaster.objects.all()
    all_urls= MenuMaster.objects.all()
    context={'service':service , 'advature':advature,"menu": all_urls}
    
    if request.method=="POST":
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        phno=request.POST.get('phno')
        address=request.POST.get('address')
        stayTo=request.POST.get('stayTo')
        stayFrom=request.POST.get('stayFrom')
        People=request.POST.get('People')
        services=request.POST.get('service')
        advature=request.POST.get('advature')
        message=request.POST.get('message')
        
        print(first_name,last_name,message,address,)
        print(advature,services,People,email,phno) 
        print(stayFrom,stayTo) 
        
        book=BookingMaster.objects.create(
            first_name=first_name, last_name=last_name,email=email , message=message, stayFrom=stayFrom , 
            stayTo=stayTo, services=services , address=address , advature=advature, phno=phno , peopel=People
        )     
        book.save()
        messages.success(request,"booking is successfully Done...!")
    return render(request,'products/booking_master.html',context)

@login_required(login_url='/accounts/login/')   
def bookview(request):
    all_urls= MenuMaster.objects.all()
    all=BookingMaster.objects.all()
    if request.GET.get('search'):
            search =request.GET.get('search')
            all=all.filter(
                Q(uid__icontains=search)|
                Q(first_name__icontains=search)|
                Q(last_name__icontains=search)|
                Q(email__icontains=search) |
                Q(phno__icontains=search) |
                Q(address__icontains=search)| 
                Q(services__icontains=search) |
                Q(advature__icontains=search)
            )
    context={'all':all, "menu": all_urls}

    if 'submit' in request.POST and request.POST['submit'] == 'delete':
        if request.method=="POST":
            bookid=request.POST.get('id')
            book=BookingMaster.objects.get(uid=bookid)
            book.delete()
            messages.error(request,"Booking is deleted")
            return HttpResponseRedirect(request.path_info)
    return render(request,"tables/bookingview.html",context)


#-------------------------------------------------------------------------------------------------------------