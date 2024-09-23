
from django.shortcuts import render
from django.contrib import messages
from Driver.models import LogisticUser
# from Driver.views import driver_homepage

from django.contrib.auth import login

def user_login(request):
    if request.method == "POST":
        email = request.POST.get('username').lower()  # Convert to lowercase for case-insensitive comparison
        password = request.POST.get('password')
        usertype = request.POST.get('usertype')
        try:
            # import pdb; pdb.set_trace()
            #check the user type
            if usertype == "admin":
                user = LogisticUser.objects.get(email=email, user_type='admin')
                if user.check_password(password):
                    request.session['user_id'] = user.id
                    request.session['user_email'] = user.email
                    request.session['user_type'] = 'admin'
                    return render(request, "admin_homepage.html",{'email': user.email})
                
                
            else:
                user = LogisticUser.objects.get(email=email, user_type='driver')
                if user.check_password(password):
                    request.session['user_id'] = user.id
                    request.session['user_email'] = user.email
                    request.session['user_type'] = 'driver'
                    return render(request, "driver_homepage.html", {'email': user.email})

        except LogisticUser .DoesNotExist:
            print(email,password)
            messages.error(request, "username or password is invalid!")
            
    
    return render(request, "login.html")



#admin-home page

def admin_home(request):
    if request.session['user_type'] == 'admin':
        return render(request, 'admin_homepage.html')
    else:
        return render(request, 'driver_homepage.html')
        



#driver-login

def driver_home(request):
    # print(request.user.is_superuser)
    return render(request, 'driver_homepage.html', {'email': request.user.email})


def driver_profile(request):
    return render(request, 'profile.html')

def driver_wallet(request):
    return render(request, 'wallet.html')