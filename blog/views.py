from django.shortcuts import render , get_object_or_404, redirect
from .models import Post
from django.utils import timezone
from .forms import PostForm
from django.contrib.auth.decorators import login_required#

def post_list(request):
    return render(request, 'blog\post_list.html',{} )

def post_list2(request):
    return render(request, 'blog\post_list2.html',{} )

def post_list3(request):
    posts = Post.objects.all()
    return render(request, 'blog\post_list3.html',{'post' : posts} )


def post_detail(request, pk):#
    posts = get_object_or_404(Post, pk=pk)#
    prev = int(pk) - 1
    next = int(pk) + 1
    return render(request, 'blog\post_detail.html',{'post' : posts, 'prev' : prev, 'next' : next} )

@login_required
def post_new(request):

    if request.method == "POST": #https method 확인
        form = PostForm(request.POST)
        if form.is_valid(): #폼 유효성 확인
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect(post_detail, pk = post.pk)
    else :
        form = PostForm()

    return render(request,'blog\post_edit.html', {'form' : form})


#from django.utils import timezone
#posts = Post.objects.filter(published_date__lte = timezone.now())
# Create your views here
