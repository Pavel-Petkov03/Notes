from django import forms
from djangoProject1.polls.models import Note


class AddNoteForm(forms.ModelForm):
    MAX_LENGTH = 30
    title = forms.CharField(max_length=50, label="Title", widget=forms.TextInput(attrs={
        'id': "id_title", "type": "text", "name": "title", "required": True, "max_length": 50
    }))

    content = forms.CharField(widget=forms.Textarea(attrs={
        'id': "id_description", "type": "text", "name": "description", "required": True, "cols": 40, "rows": 10
    }))
    image_url = forms.URLField(max_length=200, label="Link to image", widget=forms.URLInput(attrs={
        'id': "id_image_url", "type": "url", "name": "image_url", "required": True
    }))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def disable_fields(self):
        for (key, value) in self.fields.items():
            self.fields[key].widget.attrs["disabled"] = True

    class Meta:
        model = Note
        fields = "__all__"
