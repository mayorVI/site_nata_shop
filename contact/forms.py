from django import forms

from .models import Letter


class LetterForm(forms.ModelForm):

    first_name = forms.CharField(max_length=50,
                                 widget=forms.TextInput(attrs={
                                 'input type': "text",
                                 'class': "form-control",
                                 'id': "c_fname",
                                 'name': "c_fname",
    }))

    last_name = forms.CharField(max_length=50,
                                 widget=forms.TextInput(attrs={
                                 'input type': "text",
                                 'class': "form-control",
                                 'id': "c_lname",
                                 'name': "c_lname",
    }))

    email = forms.EmailField(widget=forms.EmailInput(attrs={
                                 'input type': "email",
                                 'class': "form-control",
                                 'id': "c_email",
                                 'name': "c_email",
                                 'placeholder': ""
    }))

    subject = forms.CharField(max_length=100,
                                 widget=forms.TextInput(attrs={
                                 'input type': "text",
                                 'class': "form-control",
                                 'id': "c_subject",
                                 'name': "c_subject",
    }))
    message = forms.CharField(max_length=250,
                              widget=forms.Textarea(attrs={
                                  'textarea name': "c_message",
                                  'id': "c_message",
                                  'cols': "30",
                                  'rows': "7",
                                  'class': "form-control"
    }))

    class Meta:
        model = Letter
        fields = ['first_name', 'last_name', 'email', 'subject', 'message']