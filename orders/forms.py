from django import forms

from .models import Order

class OrderCreateForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50,
                                 widget=forms.TextInput(attrs={
                                 'input type': "text",
                                 'class': "form-control",
                                 'id': "c_fname",
                                 'name': "c_fname"
    }))
    last_name = forms.CharField(max_length=50,
                                 widget=forms.TextInput(attrs={
                                 'input type': "text",
                                 'class': "form-control",
                                 'id': "c_lname",
                                 'name': "c_lname"
    }))
    phone_number = forms.CharField(max_length=20,
                                 widget=forms.TextInput(attrs={
                                 'type': "text",
                                 'class': "form-control",
                                 'id': "c_phone",
                                 'name': "c_phone",
                                 'placeholder': "Phone Number"
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
                                 'type': "text",
                                 'class': "form-control",
                                 'id': "c_email_address",
                                 'name': "c_email_address",
    }))
    address = forms.CharField(max_length=250,
                                 widget=forms.TextInput(attrs={
                                 'type': "text",
                                 'class': "form-control",
                                 'id': "c_address",
                                 'name': "c_address",
                                 'placeholder': "Street address"
    }))

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'address', 'message']
