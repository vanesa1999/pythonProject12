from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blogs/', views.BlogListView.as_view(), name ='blogs'),
    path('blog/<int:pk>', views.BlogDetailView.as_view(), name = 'blog-detail'),
    path('bloggers/', views.AuthorListView.as_view(), name = 'users'),
    path('blogger/<int:pk>', views.AuthorDetailView.as_view(),name='user-detail'),
    path('myblogs/', views.UserBlogListView.as_view(), name= 'my-blogs'),
    path('blogger/changeemail/', views.change_email, name= 'change-email'),
    path('like/<int:pk>', views.LikeView, name= 'like-blog'),
    path('blog/search/', views.SearchBlogView, name= 'search-blog'),
    path('blog/makecomment/<int:pk>', views.AddComment, name= 'add-comment'),
    path('blog/addblog/', views.AddBlog, name='add-blog'),
]