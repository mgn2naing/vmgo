from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from requests.sessions import session
from .vcenter import Vcenter
from .forms import LoginForm

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            vc = Vcenter()
            response = vc.get_session(form.cleaned_data['email'], form.cleaned_data['password'])
            if response.status_code == 200:
                r_json = response.json()
                cookie = 'vmware-api-session-id='+ r_json['value']
                resp = HttpResponseRedirect('/dashboard/index')
                resp.set_cookie('Cookie', cookie)
                return resp
            else:
                return HttpResponse('<h1 align=center>Something wrong!</h1>')
        else:
            return HttpResponse('<h1 align=center>Enter corrent information</h1>')
    else:
        if request.COOKIES.get('Cookie') is None:
            form = LoginForm()
            context = {
                'form': form
            }
            return render(request, 'vcauth/login.html', context)
        else:
            return render(request, 'dashboard/index.html')

def logout(request):
    vc = Vcenter()
    response= vc.drop_session()
    form = LoginForm()
    context = {
        'form': form
    }
    resp = render(request, 'vcauth/login.html', context)
    resp.delete_cookie('Cookie')
    return resp
