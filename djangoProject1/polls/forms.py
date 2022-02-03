# <form method="POST">
#                     <input type="hidden" name="csrfmiddlewaretoken" value="HUrRfZ1Xv8I1kg0RCRhg5I8sTJMRfcaLEI9Pf4LGjQXUjsQgoxLnWAleb0K01njw" />
#                     <label for="name">Title</label>
#                     <input type="text" name="title" maxlength="50" required="" id="id_title" />
#
#                     <label for="content">Content</label>
#                     <textarea name="description" cols="40" rows="10" required="" id="id_description"></textarea>
#
#                     <label for="image_url">Link to Image</label>
#                     <input type="url" name="image_url" maxlength="200" required="" id="id_image_url" />
#
#                     <input type="submit" value="Publish" />
#                 </form>
from django import forms


class AddNoteForm(forms.Form):
    MAX_LENGTH = 30
    title = forms.CharField(max_length=50, label="Title", widget=forms.TextInput(attrs={
        'id': "id_title", "type": "text", "name": "title", "required": True, "max_length": 50
    }))

    description = forms.CharField(widget=forms.Textarea(attrs={
        'id': "id_description", "type": "text", "name": "description", "required": True, "cols": 40, "rows": 10
    }))
    image_url = forms.ImageField(max_length=200, label="Link to image", widget=forms.ClearableFileInput(attrs={
        'id': "id_image_url", "type": "url", "name": "image_url", "required": True
    }))
