from django import forms


STATUS_CHOICES= [
    (0,'Draft'),
    (1,'Publish'),
    ]
AUTHOR_CHOICES=[
    (0,"-----"),
    ("devyani","devyani"),
]

class AddForm(forms.Form):
    title = forms.CharField(max_length=100)
    author = forms.CharField(label='Who is the author of your Blog', widget=forms.Select(choices=AUTHOR_CHOICES))
    content = forms.CharField()
    status = forms.CharField(label='What do you wanna do with your Blog', widget=forms.Select(choices=STATUS_CHOICES))


