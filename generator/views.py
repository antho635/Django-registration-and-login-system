

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
import random

from generator.models import GenPass


# Create your views here.

def password_home(request):

    if request.method == "POST":
        if query := request.POST.get('site', None):
            results = GenPass.objects.filter(site__contains=query)
            return render(request, 'generator/search.html', {'results': results})

        site = request.POST.get('site')
        user = request.user
        if site and user == "":
            return render(request, 'generator/password-home.html')

        password_length = int(request.POST.get('length'))
        if password_length > 30:
            message = "can't generate password more than 30 characters"
            context = {'message': message}
            return render(request, 'generator/password-home.html', context)
        else:
            numbers = '1234567890'
            small_letters = "qwertyuioplkjhgfdsazxcvbnm"
            prep = f"!@#$%^&**()_+{numbers}{small_letters}QWERTYUIOPASDFGHJKLMNBVCXZ"
            passwd = ''.join(random.sample(prep, k=password_length))
            print(passwd, site, user)
            p = GenPass.objects.create(site=site, user=user, passwords=passwd)
            p.save()
            context = {'password': passwd, 'user': user}
            return render(request, 'generator/success.html', context)
    return render(request, "generator/password-home.html")


@login_required
def liste_pass_generate(request):
    context = {
        'items': GenPass.objects.filter(user=request.user)
    }
    return render(request, 'generator/listalll.html', context)


def recherche(request):
    if request.method == "POST":
        if query := request.POST.get('site', None):
            results = GenPass.objects.filter(site__contains=query)
            return render(request, 'generator/search.html', {'results': results})
    return render(request, 'generator/search.html')


def delete_record(request, id):
    obj = get_object_or_404(GenPass, id=id)
    obj.delete()
    return redirect('listall')


def home_test(request):
    return render(request, 'generator/home-test.html')
