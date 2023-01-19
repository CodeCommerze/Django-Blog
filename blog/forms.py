from django import forms
from blog.models import Comment

class CommentForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea , required=True)

class ReplayForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea , required=True ) 
