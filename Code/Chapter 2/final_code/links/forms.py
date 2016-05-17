from django import forms
from captcha.fields import ReCaptchaField

from links.models import Comment


class CommentModelForm(forms.ModelForm):
    link_pk = forms.IntegerField(widget=forms.HiddenInput)
    parent_comment_pk = forms.IntegerField(widget=forms.HiddenInput, required=False)
    captcha = ReCaptchaField()

    class Meta:
        model = Comment
        fields = ('body',)