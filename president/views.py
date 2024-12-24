from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.shortcuts import redirect
from .models import Post


def logout_view(request):
    logout(request)
    return redirect('index')


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'president/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            # Return form with validation errors
            return render(request, 'president/register.html', {'form': form})
    else:
        form = UserCreationForm()
    return render(request, 'president/register.html', {'form': form})


def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
        'user_authenticated': request.user.is_authenticated,
    }
    return render(request, 'president/index.html', context)


@login_required
def create_post(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        author = request.user
        post = Post(title=title, content=content, author=author)
        post.save()
        return redirect('index')
    return render(request, 'president/create_post.html')


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'president/post_detail.html', {'post': post})


def blog_list(request):
    posts = Post.objects.all()
    return render(request, 'president/blog_list.html', {'posts': posts})


def blog_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'president/blog_detail.html', {'post': post})


def about(request):
    return render(request, 'president/about.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        return HttpResponse(f"Thank you for contacting us, {name}. We will get back to you soon!")

    return render(request, 'president/contact.html')
