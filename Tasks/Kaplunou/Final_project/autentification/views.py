from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound
from django.template.loader import render_to_string
from django.contrib.auth import logout, authenticate, login
from autentification.forms import LoginForm, RegisterForm
from django.views.generic import TemplateView

def login_user(request):
    context = {'login_form' : LoginForm()}
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('')
            else:
                context = {'login_form': LoginForm(request.POST), 'attention': f'Wrong password or username!'}


    return render(request, 'login.html', context)


class RegisterView(TemplateView):
    template_name = 'register.html'

    def get(self, request):
        user_form = RegisterForm()
        context = {'user_form' : user_form}
        return render(request, 'register.html', context)

    def post(self, request):
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            login(request, user)
            return redirect('')


def logout_user(request):
    logout(request)
    return redirect('')

#def index(request):
#    response = render_to_string('product/start_page.html')    
#    return HttpResponse(response)