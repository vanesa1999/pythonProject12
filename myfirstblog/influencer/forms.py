from django import forms
from django.contrib.auth.models import  User
from django.contrib.auth.forms import UserCreationForm


class ChangeEmailForm (forms.Form):
    changed_email= forms.EmailField(help_text="Enter your email")
    def clean_changed_email(self):
        data= self.cleaned_data['changed_email']
        return data
class BlogForm(forms.Form):
    blog_text= forms.CharField(widget=forms.Textarea)
    blog_title= forms.CharField(max_length=200)
    create_date= forms.DateTimeField(help_text="Date")
    def clean_blog_text(self):
        data= self.cleaned_data['blog_text']
        return data
    def clean_create_date(self):
        data= self.cleaned_data['create_date']
        return data
    def clean_blog_title(self):
        data= self.cleaned_data['blog_title']
        return data
class CommentForm(forms.Form):
    comment_text = forms.CharField(widget=forms.Textarea)
    comment_date= forms.DateTimeField()
    def clean_comment_text(self):
        data = self.cleaned_data['comment_text']
        return data
    def clean_comment_date(self):
        data = self.cleaned_data['comment_date']
        return data
class SearchForm(forms.Form):
    blog_title = forms.CharField(label = "Enter the Blog title you want to find",max_length =80)
    def clean_blog_title(self):
        data= self.cleaned_data['blog_title']
        return data

class NewUserForm(UserCreationForm):
    email= forms.EmailField(required=True)
    class Meta:
        model= User
        fields= ('username', 'email', 'password1', 'password2')

        def save(self, commit= True):
            user= super(NewUserForm, self).save(commit= False)
            user.email= self.cleaned_data['email']
            if commit:
                user.save()
            return user

