from django import forms
from .models import Comments,Reply

class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['blog','name','message']
        
class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['comment','name','message']