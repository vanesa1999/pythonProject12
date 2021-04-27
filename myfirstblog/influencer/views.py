from django.shortcuts import render
from .models import Blog, Author
from .models import Comment
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect , HttpResponse , request, Http404
from django.urls import reverse
from django.shortcuts import redirect
from .forms import SearchForm, CommentForm, BlogForm, ChangeEmailForm
from django.shortcuts import  render
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages #import messages
from datetime import date, datetime

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("index")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm
	return render (request=request, template_name="registration/register.html", context={"register_form":form})




def index(request):
    num_blogs= Blog.objects.all().count()
    num_authors= User.objects.all().count()
    num_visits= request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits +1
    context = {
    'num_blogs': num_blogs,
    'num_authors': num_authors,
    'num_visits': num_visits,
    }
    return render(request, 'index.html', context=context)

class BlogListView(generic.ListView):
    model= Blog
    context_object_name = 'blog_list'
    paginate_by = 5

class BlogDetailView (generic.DetailView):
    model= Blog
    def book_detail_view(request, primary_key):
        blog = get_object_or_404(Blog, pk=primary_key)
        return render(request, 'influencer/blog_detail.html', context={'blog': blog})
class AuthorListView(generic.ListView):
    model = User
    context_object_name = 'user_list'

class AuthorDetailView(generic.DetailView):
    model= User
    def author_detail_view(request, primary_key):
        user = get_object_or_404(Blog, pk=primary_key)
        return render(request, 'auth/user_detail.html', context={'user': user})

class UserBlogListView(LoginRequiredMixin, generic.ListView):
        model = User
        template_name = 'auth/userblog_list.html'

        #def get_queryset(self):
            #return Blog.objects.filter(author=self.request.user)
@login_required
def change_email (request):
    current_user = request.user
    user = User.objects.get(id=current_user.pk)
    if request.method == 'POST':
        form= ChangeEmailForm(request.POST)
        if form.is_valid():
            user.email= form.cleaned_data['changed_email']
            user.save()
            return HttpResponseRedirect( reverse('my-blogs'))
    else:
            proposed_changed_email = 'example@example.com'
            form = ChangeEmailForm(initial={'changed_email': proposed_changed_email})
    context = {
            'user': user,
            'form': form,

    }
    return render(request, 'influencer/change_email.html', context)

@login_required
def LikeView(request, pk):
    blog= Blog.objects.get(id=pk)
    blog.likes.add(request.user)
    total_likes= blog.total_likes()
    context = {
        'total_likes': total_likes,
    }
    return HttpResponseRedirect(reverse('blog-detail', args= [str(pk)]))
@login_required
def AddBlog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
                blog= Blog()
                blog.title= form.cleaned_data['blog_title']
                blog.content = form.cleaned_data['blog_text']
                blog.post_date= form.cleaned_data['create_date']
                current_user = request.user
                blog.author= current_user
                blog.save()
                return HttpResponseRedirect(reverse('my-blogs'))
    else:
        form= BlogForm()
    context = {
        'form': form,
    }
    return render(request, 'influencer/add_blog.html', context)
@login_required
def AddComment(request, pk):
    data = Blog.objects.get(id=pk)
    comments = Comment.objects.filter(blog=data)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
                com= Comment()
                com.blog= data
                com.text = form.cleaned_data['comment_text']
                com.comment_date= datetime.now()
                current_user = request.user
                com.userc= current_user
                com.save()
                return HttpResponseRedirect(reverse('blog-detail', args= [str(pk)]))
    else:
        form = CommentForm()

    context = {
        'data': data,
        'form': form,
        'comments': comments,
    }
    return render(request, 'influencer/add_comment.html', context)

def SearchBlogView(request):
    if request.method == 'POST':
        form= SearchForm(request.POST)
        if form.is_valid():
            blog_title = form.cleaned_data['blog_title']
            try:
                blog= Blog.objects.get(title= blog_title)
                pk= blog.pk
            except Blog.DoesNotExist:
                raise Http404('This blog doesnot exist')
            return HttpResponseRedirect(reverse('blog-detail', args = [str(pk)]))
    else:
        form= SearchForm()
        context ={
            'form': form
        }
    return render(request, 'influencer/SearchBook.html', context)











