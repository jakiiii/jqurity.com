from django import forms

from post.models import Post


# Create your form here.
class DateTimeInput(forms.DateTimeInput):
    input_type = 'date'


class CreatePostFrom(forms.ModelForm):

    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'image',
            'link',
            'category',
            'tags',
            'active',
            'slug',
        ]
        widgets = {
            'timestamp': DateTimeInput(),
        }

        labels = {
            'title': 'Title',
            'content': 'Content',
            'image': 'Image',
            'link': 'Link',
            'category': 'Category',
            'tags': 'Tags',
            'timestamp': 'Timestamp',
            'active': 'Active',
            'slug': 'Slug',
        }
