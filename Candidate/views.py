from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordChangeForm
from .models import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import update_session_auth_hash
from django.urls import reverse
from django.contrib import messages
from Candidate.forms import StudentUserForm,CandidateForm
# Create your views here.


@login_required
def user_logout(request):
    logout(request);
    return HttpResponseRedirect(reverse('home'))


def home(request):
    

    if request.user.is_authenticated:
       
        dict1 = Candidate.objects.filter(user=request.user)
        if len(dict1)>0:
            return render(request,'Candidate/base.html',{})
        else:
            return HttpResponse("unable to log in")
    else:
        #not logged in
        return render(request, 'Candidate/base.html')

def register(request):
    registered = False
    if request.method == "POST":
        print("hahaha")
        user_form = StudentUserForm(data=request.POST)
        info_form = CandidateForm(data=request.POST)
        if user_form.is_valid() and info_form.is_valid():
            print("lalala")
            user = user_form.save();
            user.set_password(user.password)
            user.save()
            profile = info_form.save(commit=False)
            profile.user = user;
            profile.save()
            registered = True
            if user:
                print("papapa")
                if user.is_active:
                    ("oaoaoa")
                    login(request, user)
                    return HttpResponseRedirect(reverse('home'))

                else:
                    return HttpResponse('ACCOUNT NOT ACTIVE')
            else:
                return HttpResponse("invalid login details supplied")
    else:
        user_form=StudentUserForm()
        info_form=CandidateForm()
    return render(request, 'Candidate/register_page.html', {'user_form': user_form, 'info_form': info_form, 'registered': registered, 'registerFlag': 0})


def user_login(request):
   
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)

                #to check the type of user to log in

                dict1 = Candidate.objects.filter(user=request.user)
                if len(dict1)>0:
                    return HttpResponseRedirect(reverse('home'))
                else:
                	return HttpResponse("unable to log in")

            else:
                return HttpResponse('ACCOUNT NOT ACTIVE')
        else:
            print("someone tried to login and failed")
            print("Username: {} Password: {}".format(username, password))
            return HttpResponse("invalid login details supplied")
    else:
        return render(request, 'Candidate/base.html', {})

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return HttpResponseRedirect(reverse('home'))
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'Candidate/change_password.html', {
        'form': form
    })







def ChoiceFilling(request):
    if request.POST:
        print(request.POST)
        if ("ADD" in request.POST and "choice" in request.POST):
            arr = []
            branchprefdone = []
            branches = Branch.objects.all()
            cand = Candidate.objects.get(user=request.user)
            pref = cand.preferences
            if(pref is None):
                cand.preferences = str(request.POST['choice'])
            else:
                cand.preferences=str(cand.preferences)+","+str(request.POST['choice'])
            cand.save()
            pref=cand.preferences
            if(pref):
                arr = pref.split(",")
                for x in arr:
                    temp=x.split('-')
                    if(len(temp) == 2):
                        branchprefdone.append(Branch.objects.get(name=temp[1],college=College.objects.get(name=temp[0])))
            #     branchprefdone = Branch.objects.filter(name__in=brname,college_name__in=coll)
            branchrem = []
            for x in branches:
                if x not in branchprefdone:
                    branchrem.append(x)
        elif ("REMOVE" in request.POST and "Rchoice" in request.POST):
            print(len(request.POST['Rchoice']))
            print("-----------=-=-----------=-=-=--==-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-==-==-=-=-=-=--=-=-=-")
            arr = []
            branchprefdone = []
            branches = Branch.objects.all()
            cand = Candidate.objects.get(user=request.user)
            pref = cand.preferences
            temppref=""
            if pref is not None:
                arr = pref.split(",")
                for x in arr:
                    if(x in request.POST['Rchoice']):
                        pass
                    else:
                        temppref=temppref+x
            cand.preferences=temppref
            cand.save()
            pref=temppref
            if(pref):
                arr1 = pref.split(",")
                for x in arr1:
                    temp=x.split('-')
                    if(len(temp) == 2):
                        branchprefdone.append(Branch.objects.get(name=temp[1],college=College.objects.get(name=temp[0])))
            #     branchprefdone = Branch.objects.filter(name__in=brname,college_name__in=coll)
            branchrem = []
            for x in branches:
                if x not in branchprefdone:
                    branchrem.append(x)


        else:
            arr = []
            branchprefdone = []
            branches = Branch.objects.all()
            cand = Candidate.objects.get(user=request.user)
            pref = cand.preferences
            if(pref):
                arr = pref.split(",")
                for x in arr:
                    temp=x.split('-')
                    if(len(temp) == 2):
                        branchprefdone.append(Branch.objects.get(name=temp[1],college=College.objects.get(name=temp[0])))
            branchrem = []
            for x in branches:
                if x not in branchprefdone:
                    branchrem.append(x)
    else:
        arr = []
        branchprefdone = []
        branches = Branch.objects.all()
        cand = Candidate.objects.get(user=request.user)
        pref = cand.preferences
        if(pref):
            arr = pref.split(",")
            coll = []
            brname = []
            temp = []
            for x in arr:
                temp=x.split('-')
                if(len(temp) == 2):
                    branchprefdone.append(Branch.objects.get(name=temp[1],college=College.objects.get(name=temp[0])))
        branchrem = []
        for x in branches:
            if x not in branchprefdone:
                branchrem.append(x)

    return render(request, 'Candidate/choicefilling.html',
                  {'branches': branches, 'branchprefdone': branchprefdone, 'branchrem': branchrem})


