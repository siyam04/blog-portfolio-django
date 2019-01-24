from django.contrib.auth.models import User
from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
)
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
# Same App importing
from .forms import SignUpForm, ProfileForm
from .models import Profile
# Posts App importing
from posts.models import Post


def sign_up(request):
    if request.method == 'POST':
        print('working')
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirmpassword = request.POST['repassword']
        user = User.objects.filter(username=username)
        if password == confirmpassword:
            User.objects.create_user(
                first_name = first_name,
                last_name = last_name,
                email = email,
                username = username,
                password = password
            )
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('profile-create')
    template = 'user_info/signup.html'
    return render(request, template)

def signin(request):
    if request.method == "POST":
        username, password = request.POST['username'], request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
    return redirect('home')

# @login_required(login_url='login')
# def profile_check(request):
#     try:
#         profile = Profile.objects.get(user=request.user)
#         posts = Post.objects.filter(user__profile_name=profile.profile_name)
#         context = {
#             'profile': profile,
#             'posts': posts,
#         }
#         template = 'user_info/profile_detail.html'
#         return render(request, template, context)
#     except:
#         template = 'user_info/profile_check.html'
#         return render(request, template)


def profile_create(request):
    form = ProfileForm()
    name = request.user.first_name + ' ' + request.user.last_name
    email = request.user.email
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.profile_name = name
            profile.email = email
            profile.save()
            return redirect('profile-detail', id=profile.id)
    context = {
        'form': form,
        'name': name,
        'email': email,
        }
    template = 'user_info/profile_create.html'
    return render(request, template, context)


def profile_detail(request, id=None):
    try:
        profile = get_object_or_404(Profile, id=id)
        posts = Post.objects.filter(user__profile_name=profile.profile_name)
        context = {
            'profile': profile,
            'posts': posts,
            }
        template = 'user_info/profile_detail.html'
        return render(request, template, context)
    except:
        try:
            profile = Profile.objects.get(user=request.user)
            posts = Post.objects.filter(user__profile_name=profile.profile_name)
            context = {
                'profile': profile,
                'posts': posts,
            }
            template = 'user_info/profile_detail.html'
            return render(request, template, context)
        except:
            return redirect('profile-create')


@login_required(login_url='login')
def profile_edit(request):
    profile = get_object_or_404(Profile, user=request.user)
    posts = Post.objects.filter(user__profile_name=profile.profile_name)
    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile-detail', profile.id)
    context = {
        'form': form,
        'posts': posts,
        }
    template = 'user_info/profile_edit.html'
    return render(request, template, context)
