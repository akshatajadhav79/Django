from django.shortcuts import render,HttpResponseRedirect
from staff.models import MenuMaster
from vacancy.models import VaccancyMaster, CandidateMaster
from django.contrib.auth.models import User 
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login/')   
def Candidates(request):
    candidate = CandidateMaster.objects.all()
    all_urls= MenuMaster.objects.all()
    context = {"candidate":candidate, "menu":all_urls}
    return render(request,"vacancy/Candidate.html",context)

@login_required(login_url='/login/')   
def createVacancy(request):
    all_urls= MenuMaster.objects.all()
    user=User.objects.all()
    vacancy = VaccancyMaster.objects.all()
    context = {"menu": all_urls, "user":user, "vacancy":vacancy }
    
    if request.method == "POST":
        vaccancyName = request.POST.get("vaccancyName")
        vaccancyInfo = request.POST.get("vaccancyInfo")
        vpic = request.FILES.get("vpic")
        user = request.POST.getlist("user")
        
        print(vaccancyInfo,vaccancyName, user)
        
        if VaccancyMaster.objects.filter(vaccancyName = vaccancyName ):
            messages.error(request,"Already exists")
        else:
            vacancy = VaccancyMaster.objects.create(
                vaccancyName = vaccancyName,
                vaccancyInfo = vaccancyInfo,vpic=vpic
            )
            vacancy.user.set(user)
            vacancy.save()
            messages.success(request,"Vacancy is created Successfully")   
    return render(request,"vacancy/createvacancy.html", context)

@login_required(login_url='/login/')   
def delete_v(request,id):
    v=VaccancyMaster.objects.get(vid=id)
    v.delete()
    return HttpResponseRedirect("/vacancy/createVacancy/")
 
def vshow(request):
    all_urls= MenuMaster.objects.all()
    vacancy = VaccancyMaster.objects.all()
    context = {"menu": all_urls, "vacancy":vacancy,}
    return render(request,"vacancy/vacancies.html", context)

  
def vapply(request ,id):
    v=VaccancyMaster.objects.get(vid=id)
    if request.method == "POST":
        cname = request.POST.get("cname")
        cresume = request.FILES.get("cresume")

        if CandidateMaster.objects.filter(cname = cname ):
            messages.error(request,"Already exists")
        else:
            vacancy = CandidateMaster.objects.create(
                cname = cname,
                cresume = cresume,vacancy=v
            )
            vacancy.save()
            messages.success(request,"Apply Successfully")
            return HttpResponseRedirect(request.path_info)
    
    all_urls= MenuMaster.objects.all()
    vacancy = CandidateMaster.objects.all()
    context = {"vacancy":vacancy,"v":v,"menu": all_urls}   
    
    return render(request,"vacancy/vacancyApply.html", context)

@login_required(login_url='/login/')  
def up_v(request ,id):
    uv = VaccancyMaster.objects.get(vid=id)
    vaccancyName = uv.vaccancyName
    vaccancyInfo = uv.vaccancyInfo
    user = uv.user
    
    all_urls= MenuMaster.objects.all()
    user=User.objects.all()
    vacancy = VaccancyMaster.objects.all()
    context = {"menu": all_urls, "user":user, "vacancy":vacancy }
    
    return render(request,"vacancy/createvacancy.html", context)