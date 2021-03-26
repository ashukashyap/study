from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from users.forms import profileUpdateForm, userUpdateForm
from users.models import Profile as Pro
from users.models import  Kerkesat
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from memberships.models import Membership, UserMembership, Subscription
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from blog.models import Post

# Create your views here.

def get_user_membership(request):
    user_membership_qs = UserMembership.objects.filter(user=request.user)
    if user_membership_qs.exists():
        return user_membership_qs.first()
    return None

def get_user_subscription(request):
    user_subscription_qs = Subscription.objects.filter(user_membership = get_user_membership(request))
    if user_subscription_qs.exists():
        user_subscription = user_subscription_qs.first()
        return user_subscription
    return None


@login_required
def Profile(request):
    user_membership = get_user_membership(request)
    user_subscription = get_user_subscription(request)
    if request.method == 'POST':
        u_form = userUpdateForm(request.POST,instance=request.user)
        p_form = profileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Llogaria juaj u perditsua me sukses!')
            return redirect('users:profile')
    else:
        u_form = userUpdateForm(instance=request.user)
        p_form = profileUpdateForm(instance=request.user.profile)

    context= {
        'u_form':u_form,
        'p_form':p_form,
        'user_membership':user_membership,
        'user_subscription': user_subscription
    }
    return render(request,'profile/profile.html',context)


def kerkesa(request):
    context = {} 
    if request.method == 'POST':
        email = request.POST.get('e-mail')
        name = request.POST.get('name')
        tel = request.POST.get('phone')
        try:
            em = EmailMessage(name,tel,to=[email,])
            em.send()
            context["message"] ="Email Has Been Sent"
            context["cls"] ="alert-success"
        except:
            context["message"] = "Email Could Not Sent, Please Enter Valid Email"
            context["cls"] = "alert-danger"
    return render(request,'index.html',context)
        
    

# if request.method == 'POST':
#         emri = request.POST.get('name')
#         email = request.POST.get('e-mail')
#         numri_tel = request.POST.get('phone')
#         kerkesa = Kerkesat(emri=emri, email=email, numri_tel=numri_tel)
#         kerkesa.save()
#         messages.info(request, f'Message has been sand.')
#         em = EmailMessage("Greetings","hello everone",to=["aashuk012@gmail.com"])
#         em.send()
#         return redirect('courses:home')