from django.shortcuts import redirect, render
from django.http  import HttpResponse, Http404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm,ImageUploadForm
from django.contrib.auth.decorators import login_required
from .models import Image, Profile, User, Comments

# Create your views here.
@login_required
def home_page(request):
    current_user = request.user
    posts = Image.objects.all()
    comments = Comments.objects.all()
   
    user = User.objects.get(username=current_user.username)
    users = User.objects.exclude(username=current_user.username).exclude(is_superuser=True)
  
    ctx = {
        'posts':posts,
        'user':user,
        'users':users,     
        }

    return render(request,'index.html',ctx)

@login_required
def upload_picture(request):
    current_user = request.user
    user = Profile.objects.get(user=current_user)
    if request.method == 'POST':
        form = ImageUploadForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = user
            post.save()
            return redirect('/',username=request.user)
    else:
        form = ImageUploadForm()
    return render(request,'upload_picture.html',{'form':form})

@login_required
def index(request):
    images = Image.objects.all()
    users = User.objects.exclude(id=request.user.id)
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit = False)
            image.user = request.user.profile
            image.save()
            messages.success(request, f'Successfully uploaded your pic!')
            return redirect('index')
    else:
        form = ImageUploadForm()
    return render(request, 'index.html', {"images":images[::-1], "form": form, "users": users, })

@login_required
def view_post(request,pk):
    post = Image.objects.get(id=pk)
    try:
        comments = Comments.filter_comments_by_post_id(pk)
        print(comments)
        
    except:  
        comments = None
    
    context = {
        'post':post,
        "comments":comments
        }   
    return render(request,'view_post.html',context)

@login_required
def add_comment(request,post_id):
    current_user = request.user
    if request.method == 'POST':
        comment = request.POST.get('comments')
        post = Image.objects.get(id=post_id)
        user_profile = User.objects.get(username=current_user.username)
        Comments.objects.create(comment = comment, post = post,
         user=user_profile   
        )
    return redirect('view_post', pk=post_id)    

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created you are now able to login {username}')
            return redirect('login')
    else:
       form = UserRegisterForm()
    return render(request, 'users/register.html',{"form":form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)


    context ={
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)

