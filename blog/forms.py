from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import AuthorsProfileInfo, BlogComment, BlogPost


class UserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta():
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class AuthorsProfileInfoForm(forms.ModelForm):

    class Meta():
        model = AuthorsProfileInfo
        fields = ('profile_picture', )


class PostBlog(forms.ModelForm):

    class Meta():
        model = BlogPost
        fields = ('title', 'subtitle', 'blog_post', 'image')


class CommentBlog(forms.ModelForm):

    class Meta():
        model = BlogComment
        fields = ('comment', )
