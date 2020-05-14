from django import forms
from ghostpostapp.models import PostItem

class AddPost(forms.ModelForm):
    class Meta:
        model = PostItem
        fields = ['post_title', 'body', 'boast_or_roast']
    # boast_or_roast = forms.Field(help_text="boast if clicked")