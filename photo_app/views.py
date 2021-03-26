from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from django.views import View
from .models.upload import Upload
from .models.useraccount import Useraccount
from .forms import ImageForm
from django.core.paginator import Paginator
# Create your views here.
class Index(View):
    def get(self, request):
        upload = Upload.get_all_data_from_uploads()
        paginator = Paginator(upload, 8)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, "index.html", {'upload': page_obj})

class Img_details(View):
    def get(self, request, pk):
        upload =Upload.get_img_details(pk)
        return render(request, "img_details.html", {'upload':upload})

class Signup(View):
    def get(self, request):
        return render(request, "signup.html")

    def post(self, request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = Useraccount(username=username, email=email, password=password)
        value = {
            'username': username,
            'email': email,
        }
        error_msg = None
        if not username:
            error_msg = "Username required!!"
        elif len(username) < 3:
            error_msg = "Username too small!!"
        if not email:
            error_msg = "Email required!!"
        if not password:
            error_msg = "Password required!!"
        elif len(password) < 6:
            error_msg = "Too weak password!!"
        if user.isExit():
            error_msg = "Email already exist!!"

        if not error_msg:
            user.password = make_password(user.password)
            user.user_register()
            return redirect("index")
        else:
            data = {
                'error': error_msg,
                'value': value
            }
            return render(request, 'signup.html', data)

class Login(View):
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        error_msg = None
        isemail = Useraccount.get_user_email(email)
        if isemail:
            ispassword = check_password(password, isemail.password)
            if ispassword:
                request.session['user_id'] = isemail.id
                return redirect("index")
            else:
                error_msg = "Invalid password!!"
        else:
            error_msg = "Invaild email!!"
        return render(request, "login.html", {'error':error_msg})

class Logout(View):
    def get(self, request):
        request.session.clear()
        return redirect("signup")

class Post_img(View):
    def get(self, request):
        forms = ImageForm()
        return render(request, "post_img.html", {'forms':forms})

    def post(self, request):
        forms = ImageForm(request.POST, request.FILES)
        if forms.is_valid():
            forms.save()
            return redirect("index")

class Search(View):
    def get(self, request):
        search = request.GET['search']
        data = Upload.objects.filter(name__icontains=search)
        return render(request, "search.html", {'upload': data})
