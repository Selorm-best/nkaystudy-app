from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from users.forms import profileUpdateForm, userUpdateForm
from users.models import Profile as Pro
from users.models import  TutorRequest
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from memberships.models import Membership, UserMembership, Subscription
from django.core.mail import send_mail
from django.core.mail import EmailMessage

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
            messages.success(request, 'Your account was successfully updated!')
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


def TutorRegister(request):
    if request.method == 'POST':
        code_bank = ['23456','34567','34980','5674']
        emri = request.POST.get('name')
        email = request.POST.get('e-mail')
        numri_tel = request.POST.get('phone')
        code = request.POST.get('code')
        prof = request.user.profile
        kerkesa = TutorRequest(profili=prof, emri=emri, email=email, numri_tel=numri_tel)
        kerkesa.save()
        prof_id = prof.id
        if code in code_bank:
            Pro.objects.filter(id=prof_id).update(is_teacher=True)
        
            message = 'Your request for a teacher account has been accepted! Now you can return to Nkay Study and upload courses and lectures, completed work!'
            send_mail(
                'Nkay Study, request accepted.',
                message,
                'japhethhlordjie@gmail.com',
                [email],
                fail_silently=False,
            )
            send_mail(
                'Nkay',
                'Someone made a request for the teacher''s account. With info: ' + emri + ' , ' + email + ' , ' + numri_tel + ' , ' + str(prof) + '.',
                'japhethhlordjie@gmail.com',
                ['japhethhlordjie@gmail.com'],
                fail_silently=False,
            )
            messages.info(request, f'The request was sent successfully, you will be notified by email.')
            return redirect('courses:home')
        else:
            messages.info(request, f'The code is incorrect')
            return redirect('courses:home')


