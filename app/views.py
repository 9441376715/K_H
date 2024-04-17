from django.shortcuts import render
from .forms import *
from .models import *
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,DetailView
# Create your views here.
def dummy(request):
    #UPO = UserProfile.objects.filter(user = 'a2')
    TO = Topic.objects.filter(topic_qs='a2')
    d = {'d':TO}
    print(d)
    return render(request, 'dummy.html',d)

def post(request):
    if request.method == 'POST':
        uid = request.POST['uid']
        PO = Blog_post.objects.all()
        print(PO)
        if uid in PO:
            print(True) 
        else:
            print(False)
        
def main(request):
    TO = Topic.objects.all()
    print(len(TO))
    print(TO[0])
    PO = Blog_post.objects.all()
    print(PO)
    d = {'to':TO[len(TO)-1], 'po':PO}
    if request.method == 'POST':
        uid = request.POST['uid']
        con = request.POST['con']
        PO = Blog_user.objects.all()
        print('po is : ',PO)
        return 0
        if PO[0] :
            BPO = Blog_post.objects.create(User_id = PO[0], content=con )
            BPO.save()
            TO = Topic.objects.all()
            #print('TO :', TO)
            PO = Blog_post.objects.all()
            #print('po is ',PO)
            d = {'to':TO[len(TO)-1], 'po':PO}
            return render(request, 'head.html',d)
        else:
            BUO = Blog_userForm()
            return HttpResponseRedirect(reverse('userregister'))
    return render(request,'main.html',d)
def descript(request,sid):
    TO = Topic.objects.get(pk = sid)
    ATO = Topic.objects.all()
    d = {'qo':TO, 'd': ATO}
    return render(request,'main.html', d)

def userregister(request):
    BFO = Blog_userForm()
    d = {'bfo':BFO}
    if request.method == 'POST' and request.FILES:
        bfo = Blog_userForm(request.POST, request.FILES)
        if bfo.is_valid():
            bfo.save()
            return HttpResponseRedirect(reverse('head'))
    return render(request,'userregister.html',d)

def bloguserlogin(request):
    if request.method == 'POST':
        un = request.POST['un']
        ps = request.POST['pswd']
        AU = Blog_user.objects.get_or_create(User_name = un )
        if AU[0]:
            if AU[0].password == ps :
                return HttpResponseRedirect(reverse('dummy'))
    return render(request, 'login.html')
    
    
def register(request):
    UFO = UserForm()
    PFO = UserProfileForm()
    d = {'ufo':UFO, 'pfo':PFO}
    if request.method == 'POST' and request.FILES :
        ufo = UserForm(request.POST)
        pfo = UserProfileForm(request.POST, request.FILES)
        if ufo.is_valid() and pfo.is_valid():
            mufo = ufo.save(commit = False)
            pswd = ufo.cleaned_data['password']
            mufo.set_password(pswd)
            mufo.save()
            mpfo = pfo.save(commit = False)
            mpfo.user = mufo
            mpfo.save()
            return HttpResponseRedirect(reverse('userlogin')) 
        else:
            return HttpResponse('Invalid Data')     
    return render(request, 'register.html',d)



def userlogin(request):
    if request.method == 'POST':
        username = request.POST['un']
        password = request.POST['pswd']
        AUO = authenticate(username=username, password=password)
        if AUO and AUO.is_active:
            login(request, AUO)
            request.session['username'] = username
            return render(request, 'home.html', {'un':username})
        else:
            return HttpResponse('<center>Invalid Credentials</center>')
    return render(request,'login.html')


def home(request):
    un = request.session.get('username')
    if un:
        return render(request,'home.html',{'un':un})
    return render(request, 'home.html')

@login_required
def userlogout(request):
    logout(request)
    return HttpResponseRedirect(reverse('userlogin'))

@login_required
def display_profile(request):
    un = request.session.get('username')
    uno = User.objects.get(username = un)
    po = UserProfile.objects.get(username = uno)
    d = {'un': uno, 'po':po}
    return render(request, 'display_profile.html',d)

def resetpswd(request):
    if request.method == 'POST':
        ps1 = request.POST['ps']
        rps = request.POST['rps']
        return HttpResponse('HI')
    return render(request,'resetpswd.html')

def forgotpswd(request):
    if request.method == 'POST':
        un = request.POST['un']
        uo = User.objects.get_or_create(username = un)
        if uo[0]:
            ps = request.POST['ps']
            rps = request.POST['rps']
            if ps == rps :
                uo[0].set_password(ps)
                uo[0].save()
            else:
                return render(request, 'forgotpswdermsg.html',{'ermsg':'Passwords mismatch !!'})
    return render(request, 'forgotpswd.html')
