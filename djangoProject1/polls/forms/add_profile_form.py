from django import forms
from djangoProject1.polls.models import Profile


class AddProfileForm(forms.ModelForm):
    MAX_LENGTH = 30
    first_name = forms.CharField(max_length=15, label="First Name", widget=forms.TextInput(attrs={
        'id': "id_first_name", "type": "text", "name": "first_name", "max_length": 15
    }))

    second_name = forms.CharField(max_length=15, label="Last Name", widget=forms.Textarea(attrs={
        'id': "id_last_name", "type": "text", "name": "last_name", "max_length": 15
    }))
    age = forms.IntegerField(label="Age", widget=forms.NumberInput(attrs={
        'id': "id_age", "type": "number", "name": "age",
    }))

    image_url = forms.URLField(label="Link to Profile Image", widget=forms.URLInput(attrs={
        'id': "id_image", "type": "url", "name": "profile_image",
    }))

    class Meta:
        model = Profile
        fields = "__all__"
