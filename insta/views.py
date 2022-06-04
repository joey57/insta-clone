from django.shortcuts import redirect, render
from django.http  import HttpResponse, Http404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm,ImageUploadForm
from django.contrib.auth.decorators import login_required
from .models import Image, Profile, User, Comments, Follow

# Create your views here.
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
def search_results(request):
    if 'search_profile' in request.GET and request.GET["search_profile"]:
        search_term = request.GET.get("search_profile")
        searched_profiles = Profile.search_profile(search_term)
        print(searched_profiles)
        message = f"{search_term}"
        return render(request, 'search_results.html', {"message":message,"profiles": searched_profiles})
    else:
        message = "You haven't searched for any profile"
    return render(request, 'search_results.html', {'message': message})

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

@login_required
def follow(request,id):
    if request.method == 'GET':
        user_follow=User.objects.get(pk=id)
        follow_user=Follow(follower=request.user, followed=user_follow)
        follow_user.save()
        return redirect('user_profile' ,username=user_follow.username)

@login_required    
def unfollow(request,id):
    if request.method=='GET':
        user_unfollow=User.objects.get(pk=id)
        unfollow_user=Follow.objects.filter(follower=request.user,followed=user_unfollow)
        unfollow_user.delete()
        return redirect('user_profile' ,username=user_unfollow.username)    

@login_required
def user_profile(request, username):
    current_user = request.user
    user= User.objects.get(username = current_user.username)
    user_select = User.objects.get(username=username)
    if user_select == user:
        return redirect('profile', username=request.user.username)
    posts = Image.objects.filter(user = user_select.id)
    profile = Profile.filter_profile_by_id(follower_is = user_select.id)
    followers = Follow.objects.filter(followed=user_select.id)

    follow_status = False
    for follower in followers:
        if user.id == follower.follower.id:
            follow_status = True
            break 
        else:
            follow_status = False

    context ={
        'posts': posts,
        'profile':profile,
        'user':user,
        'user_select':user_select,
        'followers':followers,
        'follow_status':follow_status,
    }           
    return render(request, 'user_profile.html', context)

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

