from django.contrib.auth.models import User
from django.views.generic import CreateView
from .forms import BaseRegisterForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
import random
from django.shortcuts import render
from .models import Preuser

class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    template_name = 'sign/signup.html'

    __tmp_password = ""

    def post(self, request, *args, **kwargs):
        self.__tmp_password = request.POST['password1']
        return super(BaseRegisterView, self).post(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.instance
        Preuser.objects.create(code=str(random.randint(0, 10000)), username=user.username,
                        email=user.email, password=self.__tmp_password)
        return redirect('/sign/signup_confirm')

def register_confirm_view(request):
    if request.method == 'POST':
        code = request.POST['code']
        if Preuser.objects.filter(code=code).exists():
            user = Preuser.objects.get(code=code)
            User.objects.create_user(user.username, user.email, user.password)
            return redirect('/sign/login')
    return render(request, 'sign/signup_confirm.html')

class BaseLoginView(LoginView):
    template_name = 'sign/login.html'

class BaseLogoutView(LogoutView):
    template_name = 'sign/logout.html'
